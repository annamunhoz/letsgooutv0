CREATE TABLE public."PLACES"
(
    "ID" serial PRIMARY KEY,
    name character varying(250) NOT NULL,
    price character varying(100) NOT NULL,
    category character varying(500) NOT NULL
)