# this file is used for local development
# it links the syntest-core libraries to the benchmark libraries
# it links the syntest-javascript libraries to the benchmark libraries

rm -rf node_modules/@syntest/*

cd node_modules/@syntest

# core libraries
ln -s ../../../syntest-core/libraries/analysis analysis
ln -s ../../../syntest-core/libraries/cfg cfg
ln -s ../../../syntest-core/libraries/cli-graphics cli-graphics
ln -s ../../../syntest-core/libraries/logging logging
ln -s ../../../syntest-core/libraries/metric metric
ln -s ../../../syntest-core/libraries/module module
ln -s ../../../syntest-core/libraries/search search
ln -s ../../../syntest-core/libraries/storage storage
ln -s ../../../syntest-core/libraries/prng prng

# core plugins
ln -s ../../../syntest-core/plugins/plugin-core-event-listener-graphing plugin-core-event-listener-graphing
ln -s ../../../syntest-core/plugins/plugin-core-event-listener-state-storage plugin-core-event-listener-state-storage
ln -s ../../../syntest-core/plugins/plugin-core-event-listener-websocket plugin-core-event-listener-websocket
ln -s ../../../syntest-core/plugins/plugin-core-metric-middleware-file-writer plugin-core-metric-middleware-file-writer
ln -s ../../../syntest-core/plugins/plugin-core-metric-middleware-statistics plugin-core-metric-middleware-statistics
ln -s ../../../syntest-core/plugins/plugin-core-search-algorithm-experimental plugin-core-search-algorithm-experimental

# core tools
ln -s ../../../syntest-core/tools/cli cli
ln -s ../../../syntest-core/tools/base-language base-language
ln -s ../../../syntest-core/tools/init init

# javascript libraries
ln -s ../../../syntest-javascript/libraries/analysis-javascript analysis-javascript
ln -s ../../../syntest-javascript/libraries/ast-visitor-javascript ast-visitor-javascript
ln -s ../../../syntest-javascript/libraries/instrumentation-javascript instrumentation-javascript
ln -s ../../../syntest-javascript/libraries/search-javascript search-javascript

# javascript plugins
ln -s ../../../syntest-javascript/plugins/plugin-javascript-event-listener-state-storage plugin-javascript-event-listener-state-storage

# javascript tools
ln -s ../../../syntest-javascript/tools/javascript javascript
