--
-- PostgreSQL database dump
--

-- Dumped from database version 12.0
-- Dumped by pg_dump version 12.0

-- Started on 2019-11-16 20:28:23

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 203 (class 1259 OID 32896)
-- Name: animals; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.animals (
    id integer NOT NULL,
    animal_name character varying,
    species character varying
);


ALTER TABLE public.animals OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 32894)
-- Name: animals_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.animals_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.animals_id_seq OWNER TO postgres;

--
-- TOC entry 2824 (class 0 OID 0)
-- Dependencies: 202
-- Name: animals_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.animals_id_seq OWNED BY public.animals.id;


--
-- TOC entry 2688 (class 2604 OID 32899)
-- Name: animals id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.animals ALTER COLUMN id SET DEFAULT nextval('public.animals_id_seq'::regclass);


--
-- TOC entry 2818 (class 0 OID 32896)
-- Dependencies: 203
-- Data for Name: animals; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.animals (id, animal_name, species) FROM stdin;
1	Mickey Mouse	mouse
2	Minnie Mouse	mouse
3	Donald Duck	duck
\.


--
-- TOC entry 2825 (class 0 OID 0)
-- Dependencies: 202
-- Name: animals_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.animals_id_seq', 1, false);


--
-- TOC entry 2690 (class 2606 OID 32904)
-- Name: animals animals_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.animals
    ADD CONSTRAINT animals_pkey PRIMARY KEY (id);


-- Completed on 2019-11-16 20:28:23

--
-- PostgreSQL database dump complete
--

