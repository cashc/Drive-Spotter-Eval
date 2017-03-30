CREATE TABLE public.users
(
  id         SERIAL PRIMARY KEY NOT NULL,
  username      VARCHAR(128),
  firstname VARCHAR(64),
  lastname  VARCHAR(64),
  hash       VARCHAR(66)
);
CREATE UNIQUE INDEX users_id_uindex
  ON public.users (id);
CREATE UNIQUE INDEX users_username_uindex
  ON public.users (username);
