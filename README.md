# Syntest JavaScript Benchmark



## Building the docker container
Building
```bash
docker build --tag="syntest/javascript:new" .
```

Running
```bash
docker run --env time_per_target=5 --env incorporate_execution_information=true --env type_inference_mode="proportional" --env target_root_directory="./commanderjs" --env include="./commanderjs/lib/**/*.js" syntest/javascript:new
```
