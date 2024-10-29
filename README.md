Create locally timescaledb database

```bash
createdb -h localhost -p 5432 -U postgres timescaledb
```

Run timescaledb via docker

> [Difference between timescaledb and timescaledb-ha](https://stackoverflow.com/questions/77084310/weird-uuid-behavior-after-switching-to-timescaledb-ha)

```bash
docker pull timescale/timescaledb-ha:pg16
docker run -d --name timescaledb -p 5432:5432 -e POSTGRES_PASSWORD=password timescale/timescaledb-ha:pg16
```
