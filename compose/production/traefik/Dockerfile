FROM docker.io/traefik:2.9
RUN mkdir -p /etc/traefik/acme \
  && touch /etc/traefik/acme/acme.json \
  && chmod 600 /etc/traefik/acme/acme.json \
  && adduser -s /bin/false -D -H traefik
COPY ./compose/production/traefik/traefik.yml /etc/traefik

EXPOSE 8080 8443
