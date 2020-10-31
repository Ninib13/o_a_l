FROM alpine:3.12
COPY 3.sh ./3.sh
RUN chmod +x ./3.sh && sh ./3.sh
CMD ["/bin/sh"]