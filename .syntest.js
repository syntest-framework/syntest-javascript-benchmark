module.exports = {
    // seed: 'test',
    "population-size": 50,
    "max-depth": 5,

    // mutation chances
    "resample-gene-probability": 0.01,
    "delta-mutation-probability": 0.8,
    "sample-func-as-arg": 0.5,
    "explore-illegal-values": false,

    "algorithm": "DynaMOSA",
    "search-time-budget": 30,
    "total-time-budget": 30,
    "iteration-budget": 1000000,

    "constant-pool": true,
    "constant-pool-probability": 0.5,

    // logging
    "console-log-level": "info",
    "log-to-file": ["info", "warn", "error"],

    "incorporate-execution-information": true,
    "type-inference-mode": 'proportional', // none proportional ranked
    "random-type-probability": 0.1,

    "draw-cfg": false,
    "target-root-directory": "./commanderjs",

    // target-root-directory: "./axios",
    "target-root-directory": "./commanderjs",
    // target-root-directory: "./express",
    // target-root-directory: "./lodash",
    // target-root-directory: "./moment/src",

    // target-root-directory: "./javascript-algorithms",

    // target-root-directory: "./chalk",
    // target-root-directory: "./jquery",
    // target-root-directory: "./npm-cli",

    "include": [
        // "./axios/lib/core/buildFullPath.js",
        // "./axios/lib/core/Axios.js",

        "./commanderjs/lib/help.js",

        // "./lodash/.internal/equalArrays.js",
        // "./lodash/hasPath.js",
        // "./lodash/random.js",
        // "./lodash/result.js",
        // "./lodash/slice.js",
        // "./lodash/split.js",
        // "./lodash/toNumber.js",
        // "./lodash/transform.js",
        // "./lodash/truncate.js",
        // "./lodash/unzip.js",


        // "./express/lib/view.js",

        // "./axios/lib/core/*.js",
        // "./commanderjs/lib/**/*.js",

        // "./express/lib/**/*.js",
        // "./lodash/**/*.js",
        // "./moment/src/lib/create/**/*.js",
        // "./moment/src/lib/moment/**/*.js",

        // "./javascript-algorithms/src/data-structures/tree/red-black-tree/*.js",
        // "./javascript-algorithms/src/algorithms/math/matrix/*.js",
        // "./javascript-algorithms/src/algorithms/sorting/counting-sort/*.js",
        // "./javascript-algorithms/src/algorithms/graph/**/*.js",
        // "./javascript-algorithms/src/algorithms/sets/knapsack-problem/*.js"

        // "./javascript-algorithms/src/algorithms/graph/detect-cycle/detectUndirectedCycleUsingDisjointSet.js",


        // "./chalk/source/**/*.js",
        // "./jquery/src/core/**/*.js",
        // "./npm_cli/lib/auth/*.js",


    ],
    "exclude": [
        './lodash/test/.internal/*.js',
        './lodash/test/**/*.js',

        "./commanderjs/lib/argument.js",
        "./commanderjs/lib/command.js",
        "./commanderjs/lib/error.js",

        "./express/lib/router/index.js",
        "./express/lib/express.js",

        "./moment/src/lib/create/local.js",
        "./moment/src/lib/create/utc.js",

        "./moment/src/lib/moment/clone.js",
        "./moment/src/lib/moment/creation-data.js",
        "./moment/src/lib/moment/valid.js",
        "./moment/src/lib/moment/moment.js"

        // "./chalk/source/vendor/supports-color/*.*",

    ]
}
