#!/bin/bash

docker exec postgres_db pg_dump -U admin appdb > backup.sql