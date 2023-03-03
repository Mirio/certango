FROM docker.io/alpine:3.17

ENV USER_UID "1000"
ENV USER_GID "1000"
ENV USER_NAME "certargo"
ENV USER_HOME "/home/${USER_NAME}"
ENV BUILD_ENVIRONMENT "production"
ENV BUILD_ENV "${BUILD_ENVIRONMENT}"

USER 0
RUN apk add --no-cache alpine-sdk bash gettext libpq-dev py3-virtualenv python3-dev tzdata \
    && addgroup -g "${USER_GID}" "${USER_NAME}" && adduser -G "${USER_NAME}" -u "${USER_UID}" -D "${USER_NAME}"

USER "${USER_UID}"
WORKDIR "/home/${USER_NAME}"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV BUILD_ENV ${BUILD_ENVIRONMENT}

COPY --chown="${USER_UID}":"${USER_UID}" "*.py" "LICENSE" "setup.cfg" "${USER_HOME}"
COPY --chown="${USER_UID}":"${USER_UID}" "./requirements" "${USER_HOME}/requirements"
COPY --chown="${USER_UID}":"${USER_UID}" "./certango" "${USER_HOME}/certango"
COPY --chown="${USER_UID}":"${USER_UID}" "./config" "${USER_HOME}/config"
COPY --chown="${USER_UID}":"${USER_UID}" "./tests" "${USER_HOME}/tests"
COPY --chown="${USER_UID}":"${USER_UID}" "./locale" "${USER_HOME}/locale"
COPY --chown="${USER_UID}":"${USER_UID}" "./compose/production/django/start.bash" "${USER_HOME}/start.bash"

RUN python3 -m venv "${USER_HOME}/.venv" && source "${USER_HOME}/.venv/bin/activate" \
    && pip install --upgrade pip && pip install --no-cache-dir -r "${USER_HOME}/requirements/${BUILD_ENVIRONMENT}.txt" \
    && rm -rf "${USER_HOME}/.cache" && chmod +x "${USER_HOME}/start.bash"

VOLUME ["/data"]
EXPOSE 8000

CMD ["./start.bash"]
