module.exports = {
    // seed: 'test',
    population_size: 50,
    max_depth: 5,

    // mutation chances
    resample_gene_probability: 0.01,
    delta_mutation_probability: 0.8,
    sample_func_as_arg: 0.5,
    explore_illegal_values: false,

    algorithm: "DynaMOSA",
    search_time: 5,
    total_time: 60000,
    iteration_budget: 1000000,

    probe_objective: true,
    modifier_extraction: true,
    constant_pool: true,
    constant_pool_probability: 0.5,

    // logging
    console_log_level: "info",
    log_to_file: ["info", "warn", "error"],

    incorporate_execution_information: true,
    type_inference_mode: 'proportional', // none proportional ranked
    random_type_probability: 0.1,

    draw_cfg: false,


    // target_root_directory: "./axios",
    target_root_directory: "./commanderjs",
    // target_root_directory: "./express",
    // target_root_directory: "./lodash",
    // target_root_directory: "./moment/src",

    // target_root_directory: "./javascript-algorithms",

    // target_root_directory: "./chalk",
    // target_root_directory: "./jquery",
    // target_root_directory: "./npm_cli",

    include: [
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
    exclude: [
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
