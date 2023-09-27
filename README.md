# Syntest JavaScript Benchmark

This repository contains a benchmark that can be used to evaluate SynTest Framework - JavaScript.

## Running Instructions

1. Clone the `benchmark` project:
```bash
git clone git@github.com:syntest-framework/syntest-javascript-benchmark.git
```

2. Move into the `benchmark` project and install the dependencies
```bash
cd syntest-javascript-benchmark
npm install
```
> Note: this will also initiate the git submodules and install dependencies of the benchmark projects


3. Run the tool
```bash
npx syntest javascript test
```

## Local (Development) Running Instructions

1. Create a local working directory:
```bash
mkdir syntest
cd syntest
```

2. Clone all projects (i.e., `core`, `javascript`, and `benchmark`) in the same directory:
```bash
git clone git@github.com:syntest-framework/syntest-core.git
git clone git@github.com:syntest-framework/syntest-javascript.git
git clone git@github.com:syntest-framework/syntest-javascript-benchmark.git
```

3. Move into the `core` project, install all the dependencies, and build the project to compile all the TypeScript code:
```bash
cd syntest-core
npm install
npm run build
```

4. Move into the `javascript` project, install all the dependencies, link the dependencies contained within the `core` to the local version, and build the project to compile all the TypeScript code.
```bash
cd syntest-javascript
npm install
./link.sh
npm run build
```

5. Move into the `benchmark` project and call the local:install script:
```bash
cd syntest-javascript-benchmark
npm run local:install
```
This will link the core and javascript project to the current node_modules folder.
> Note: this will also initiate the git submodules and install dependencies of the benchmark projects.

7. Run the tool
```bash
npx syntest javascript test
```

## Configuration

### Benchmark Project Selection

The file `.syntest-projects.json` contains the different configurations needed to run the various benchmarks contained in this project:

- CommanderJS
- Express
- JavaScript Algorithms
- Lodash
- Moment

These configurations can be manually provided on the CLI or pasted into the `.syntest.json` config. As basic configuration is provided by default in the `.syntest.json` config.

### Search Algorithm Selection

There are various presets:
- DynaMOSA
- MOSA
- NSGAII

That configure all the parameters for that algorithm.

Additionally, users can configure all parameters themselves by providing the individual configuration paramaters:
- search-algorithm
- population-size
- objective-manager
- secondary-objective
- crossover
- procreation
- sampler

### Search Budget Selection

By default the search algorithm will run until all objectives are covered. It is recommanded to provide an additional search budget that constraints the time the search algorithm has. The framework provides the following budgets:
- total-time
- search-time
- iterations
- evaluations
