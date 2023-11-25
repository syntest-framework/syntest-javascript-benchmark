FROM node:lts

# set environment variables for run time
ENV target_root_directory=
ENV target_include=
ENV analysis_include=
ENV preset=
ENV time=

# clone the repos
WORKDIR /app/
# Replace by the fork
RUN git clone https://github.com/syntest-framework/syntest-framework.git
WORKDIR /app/syntest-framework
RUN git fetch
RUN git checkout implement-decorators
WORKDIR /app/
RUN git clone https://github.com/syntest-framework/syntest-javascript.git
WORKDIR /app/syntest-javascript
RUN git fetch
RUN git checkout feat-implement-decorators
WORKDIR /app/
RUN git clone https://github.com/syntest-framework/syntest-javascript-benchmark.git

# Install and build core
WORKDIR /app/syntest-framework
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
RUN npm run local:install

CMD timeout -k 25m 25m npx syntest javascript test --target-root-directory=${target_root_directory} --target-include=${include} --analysis-include=${analysis_include} --preset=${preset} --total-time=${time}
