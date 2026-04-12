#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd -- "${SCRIPT_DIR}/.." && pwd)"
ENV_FILE="${REPO_ROOT}/.env"

if [[ ! -f "${ENV_FILE}" ]]; then
  echo "Error: ${ENV_FILE} was not found." >&2
  exit 1
fi

# shellcheck disable=SC1090
source "${ENV_FILE}"

APP_ID="${CB_APP_ASSISTANT_APP_ID:-}"
INSTALLATION_ID="${CB_APP_ASSISTANT_INSTALLATION_ID:-}"
PRIVATE_KEY_PATH="${CB_APP_ASSISTANT_PRIVATE_KEY_PATH:-}"

if [[ -z "${APP_ID}" || -z "${INSTALLATION_ID}" || -z "${PRIVATE_KEY_PATH}" ]]; then
  echo "Error: missing one or more required env vars: CB_APP_ASSISTANT_APP_ID, CB_APP_ASSISTANT_INSTALLATION_ID, CB_APP_ASSISTANT_PRIVATE_KEY_PATH." >&2
  exit 1
fi

if [[ ! -f "${PRIVATE_KEY_PATH}" ]]; then
  echo "Error: private key file not found at ${PRIVATE_KEY_PATH}." >&2
  exit 1
fi

if [[ $# -lt 2 ]]; then
  echo "Usage: $0 <issue_number> <comment_body>" >&2
  exit 1
fi

ISSUE_NUMBER="$1"
shift
COMMENT_BODY="$*"
REPO="Civic-Blueprint/project-2028"

base64url() {
  openssl base64 -A | tr '+/' '-_' | tr -d '='
}

IAT="$(date +%s)"
EXP="$((IAT + 540))"

JWT_HEADER="$(printf '{"alg":"RS256","typ":"JWT"}' | base64url)"
JWT_PAYLOAD="$(printf '{"iat":%d,"exp":%d,"iss":"%s"}' "${IAT}" "${EXP}" "${APP_ID}" | base64url)"
JWT_SIGNATURE="$(
  printf '%s.%s' "${JWT_HEADER}" "${JWT_PAYLOAD}" \
  | openssl dgst -sha256 -sign "${PRIVATE_KEY_PATH}" -binary \
  | base64url
)"
JWT="${JWT_HEADER}.${JWT_PAYLOAD}.${JWT_SIGNATURE}"

TOKEN_RESPONSE="$(
  curl -sS -X POST \
    -H "Authorization: Bearer ${JWT}" \
    -H "Accept: application/vnd.github+json" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    "https://api.github.com/app/installations/${INSTALLATION_ID}/access_tokens"
)"

INSTALLATION_TOKEN="$(
  TOKEN_RESPONSE="${TOKEN_RESPONSE}" python3 - <<'PY'
import json
import os
import sys

payload = os.environ["TOKEN_RESPONSE"]
try:
    data = json.loads(payload)
except json.JSONDecodeError:
    print("")
    sys.exit(0)
print(data.get("token", ""))
PY
)"

if [[ -z "${INSTALLATION_TOKEN}" ]]; then
  echo "Error: failed to acquire installation token." >&2
  echo "Response: ${TOKEN_RESPONSE}" >&2
  exit 1
fi

COMMENT_JSON="$(
  COMMENT_BODY="${COMMENT_BODY}" python3 - <<'PY'
import json
import os

print(json.dumps({"body": os.environ["COMMENT_BODY"]}))
PY
)"

COMMENT_RESPONSE="$(
  curl -sS -X POST \
    -H "Authorization: Bearer ${INSTALLATION_TOKEN}" \
    -H "Accept: application/vnd.github+json" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    "https://api.github.com/repos/${REPO}/issues/${ISSUE_NUMBER}/comments" \
    -d "${COMMENT_JSON}"
)"

COMMENT_URL="$(
  COMMENT_RESPONSE="${COMMENT_RESPONSE}" python3 - <<'PY'
import json
import os
import sys

payload = os.environ["COMMENT_RESPONSE"]
try:
    data = json.loads(payload)
except json.JSONDecodeError:
    print("")
    sys.exit(0)
print(data.get("html_url", ""))
PY
)"

if [[ -z "${COMMENT_URL}" ]]; then
  echo "Error: failed to create comment." >&2
  echo "Response: ${COMMENT_RESPONSE}" >&2
  exit 1
fi

echo "Posted comment as bot: ${COMMENT_URL}"
