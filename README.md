# Syntest JavaScript Benchmark



## Building the docker container
Building
```bash
docker build --tag="syntest/javascript:new" .
```

Running
```bash
docker run --env time_per_target=5 --env use_type_inference=1 --env type_inference_mode="proportional" --env target_root_directory="./benchmark/top10npm/axios" --env include="./benchmark/top10npm/axios/lib/**/*.js" syntest/javascript:new
```
