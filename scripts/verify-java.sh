#!/usr/bin/env bash
# Runs the project's build and tests and prints only the summary. Uses no tokens.
set -uo pipefail
log=$(mktemp)
trap 'rm -f "$log"' EXIT
if [ -x ./mvnw ]; then cmd=(./mvnw -B -q verify)
elif [ -f pom.xml ]; then cmd=(mvn -B -q verify)
elif [ -x ./gradlew ]; then cmd=(./gradlew --console=plain check)
elif [ -f build.gradle ] || [ -f build.gradle.kts ]; then cmd=(gradle --console=plain check)
else echo "NO_BUILD: pom.xml or build.gradle not found in $(pwd)"; exit 2; fi
echo "RUN: ${cmd[*]}"
"${cmd[@]}" >"$log" 2>&1
code=$?
grep -E 'Tests run:.*Fail|BUILD (SUCCESS|FAILURE|SUCCESSFUL|FAILED)|\[ERROR\].*(FAIL|Failed tests|Tests in error)|tests completed' "$log" | tail -25
if [ "$code" -ne 0 ]; then echo "--- last lines ---"; tail -25 "$log"; fi
echo "EXIT: $code"
exit "$code"
