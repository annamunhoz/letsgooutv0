-- Table: public."PLACES"

-- DROP TABLE public."PLACES";

CREATE TABLE public."PLACES"
(
    "ID" integer NOT NULL DEFAULT nextval('"PLACES_ID_seq"'::regclass),
    name character varying(250) COLLATE pg_catalog."default" NOT NULL,
    price character varying(100) COLLATE pg_catalog."default" NOT NULL,
    category character varying(500) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "PLACES_pkey" PRIMARY KEY ("ID")
)