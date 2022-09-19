FROM node:16.13

# set environment variables for run time
ENV time_per_target=
ENV incorporate_execution_information=
ENV type_inference_mode=
ENV target_root_directory=
ENV include=

WORKDIR /app/syntest-framework
COPY ../syntest-framework .
RUN npm install
RUN npm run build

WORKDIR /app/syntest-javascript
COPY ../syntest-javascript .
RUN npm install
RUN npm run build
RUN npm install -g .

WORKDIR /app/syntest-javascript-benchmark
COPY . .
RUN npm install

# Install benchmark dependencies
WORKDIR /app/syntest-javascript-benchmark/express
RUN npm install

WORKDIR /app/syntest-javascript-benchmark

ENTRYPOINT syntest-javascript --search_time=${time_per_target} --incorporate_execution_information=${incorporate_execution_information} --type_inference_mode=${type_inference_mode} --target_root_directory=${target_root_directory} --include=${include}

