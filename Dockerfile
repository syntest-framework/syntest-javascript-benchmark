FROM node:lts

# set environment variables for run time
ENV target_root_directory=
ENV include=
ENV preset=

# clone the repos
WORKDIR /app/
# Replace by the fork
RUN git clone https://github.com/syntest-framework/syntest-core.git 
RUN git clone https://github.com/syntest-framework/syntest-javascript.git
RUN git clone https://github.com/syntest-framework/syntest-javascript-benchmark.git

# Install and build core
WORKDIR /app/syntest-core
RUN npm install
RUN npm run build

# Install, link and build javascript
WORKDIR /app/syntest-javascript
RUN npm install
RUN ./link.sh
RUN npm run build

# Install benchmark
WORKDIR /app/syntest-javascript-benchmark
COPY .syntest.json .
RUN npm install

# Install benchmark dependencies
WORKDIR /app/syntest-javascript-benchmark/benchmark/express
RUN npm install

WORKDIR /app/syntest-javascript-benchmark

CMD npx syntest javascript test --target-root-directory=${target_root_directory} --include=${include} --preset=${preset}
