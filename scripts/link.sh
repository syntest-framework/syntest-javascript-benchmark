# this file is used for local development
# it links the syntest-framework libraries to the benchmark libraries
# it links the syntest-javascript libraries to the benchmark libraries

rm -rf node_modules/@syntest/*

cd node_modules/@syntest

# core libraries
ln -s ../../../syntest-framework/libraries/analysis analysis
ln -s ../../../syntest-framework/libraries/cfg cfg
ln -s ../../../syntest-framework/libraries/cli-graphics cli-graphics
ln -s ../../../syntest-framework/libraries/logging logging
ln -s ../../../syntest-framework/libraries/metric metric
ln -s ../../../syntest-framework/libraries/module module
ln -s ../../../syntest-framework/libraries/search search
ln -s ../../../syntest-framework/libraries/storage storage
ln -s ../../../syntest-framework/libraries/prng prng

# core plugins
ln -s ../../../syntest-framework/plugins/plugin-event-listener-graphing plugin-event-listener-graphing
ln -s ../../../syntest-framework/plugins/plugin-event-listener-state-storage plugin-event-listener-state-storage
ln -s ../../../syntest-framework/plugins/plugin-event-listener-websocket plugin-event-listener-websocket
ln -s ../../../syntest-framework/plugins/plugin-metric-middleware-file-writer plugin-metric-middleware-file-writer
ln -s ../../../syntest-framework/plugins/plugin-metric-middleware-statistics plugin-metric-middleware-statistics
ln -s ../../../syntest-framework/plugins/plugin-search-algorithm-experimental plugin-search-algorithm-experimental

# core tools
ln -s ../../../syntest-framework/tools/cli cli
ln -s ../../../syntest-framework/tools/base-language base-language
ln -s ../../../syntest-framework/tools/init init

# javascript libraries
ln -s ../../../syntest-javascript/libraries/analysis-javascript analysis-javascript
ln -s ../../../syntest-javascript/libraries/ast-visitor-javascript ast-visitor-javascript
ln -s ../../../syntest-javascript/libraries/instrumentation-javascript instrumentation-javascript
ln -s ../../../syntest-javascript/libraries/search-javascript search-javascript

# javascript plugins
ln -s ../../../syntest-javascript/plugins/plugin-javascript-event-listener-state-storage plugin-javascript-event-listener-state-storage

# javascript tools
ln -s ../../../syntest-javascript/tools/javascript javascript

chmod +x ../.bin/syntest