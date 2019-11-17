--
-- PostgreSQL database dump
--

-- Dumped from database version 12.0
-- Dumped by pg_dump version 12.0

-- Started on 2019-11-16 20:01:05

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
-- TOC entry 203 (class 1259 OID 32878)
-- Name: departments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.departments (
    id integer NOT NULL,
    dept_name character varying
);


ALTER TABLE public.departments OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 32870)
-- Name: employees; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.employees (
    employee_id integer NOT NULL,
    first_name character varying,
    last_name character varying,
    department_id integer
);


ALTER TABLE public.employees OWNER TO postgres;

--
-- TOC entry 2822 (class 0 OID 32878)
-- Dependencies: 203
-- Data for Name: departments; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.departments (id, dept_name) FROM stdin;
45	webdev
\.


--
-- TOC entry 2821 (class 0 OID 32870)
-- Dependencies: 202
-- Data for Name: employees; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.employees (employee_id, first_name, last_name, department_id) FROM stdin;
14	Jan	Jansson	45
\.


--
-- TOC entry 2694 (class 2606 OID 32885)
-- Name: departments departments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.departments
    ADD CONSTRAINT departments_pkey PRIMARY KEY (id);


--
-- TOC entry 2692 (class 2606 OID 32877)
-- Name: employees employees_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.employees
    ADD CONSTRAINT employees_pkey PRIMARY KEY (employee_id);


-- Completed on 2019-11-16 20:01:06

--
-- PostgreSQL database dump complete
--

