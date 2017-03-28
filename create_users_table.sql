CREATE TABLE public.users
(
  id         SERIAL PRIMARY KEY NOT NULL,
  email      VARCHAR(128),
  firstname VARCHAR(64),
  lastname  VARCHAR(64),
  hash       VARCHAR(64)
);
CREATE UNIQUE INDEX users_id_uindex
  ON public.users (id);
CREATE UNIQUE INDEX users_email_uindex
  ON public.users (email);
