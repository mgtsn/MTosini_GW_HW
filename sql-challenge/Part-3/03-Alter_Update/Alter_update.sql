--
-- PostgreSQL database dump
--

-- Dumped from database version 12.0
-- Dumped by pg_dump version 12.0

-- Started on 2019-11-16 20:19:37

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
-- TOC entry 202 (class 1259 OID 32887)
-- Name: employees; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employees (
    employee_id integer,
    first_name character varying,
    last_name character varying,
    dept_id integer,
    annual_salary double precision
);


ALTER TABLE public.employees OWNER TO postgres;

--
-- TOC entry 2812 (class 0 OID 32887)
-- Dependencies: 202
-- Data for Name: employees; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.employees (employee_id, first_name, last_name, dept_id, annual_salary) FROM stdin;
3	Chris	Christian	25	\N
14	Jan	Jansson	45	\N
17	Sam	Samuels	45	\N
\.


-- Completed on 2019-11-16 20:19:38

--
-- PostgreSQL database dump complete
--

