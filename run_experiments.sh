experiment_name="new"
time=120

incorporate_execution_information=( true false ) # false
modes=( "none" "ranked" "proportional" ) # none ranked proportional
benchmark_name=(
"javascript_algorithms_matrix"
"javascript_algorithms_sort"
"javascript_algorithms_tree"
"javascript_algorithms_knapsack"
"javascript_algorithms_graph"
"axios"
"commanderjs"
"express"
"moment"
"moment"
"lodash"
"lodash"
"lodash"
"lodash"
"lodash"
"lodash"
"lodash"
"lodash"
"lodash"
"lodash" )
benchmarks=(
"javascript-algorithms"
"javascript-algorithms"
"javascript-algorithms"
"javascript-algorithms"
"javascript-algorithms"
"axios"
"commanderjs"
"express"
"moment/src"
"moment/src"
"lodash"
"lodash"
"lodash"
"lodash"
"lodash"
"lodash"
"lodash"
"lodash"
"lodash"
"lodash" )
benchmark_files=(
"javascript-algorithms/src/algorithms/math/matrix/*.js"
"javascript-algorithms/src/algorithms/sorting/counting-sort/*.js"
"javascript-algorithms/src/data-structures/tree/red-black-tree/*.js"
"javascript-algorithms/src/algorithms/sets/knapsack-problem/*.js"
"javascript-algorithms/src/algorithms/graph/**/*.js"
"axios/lib/core/*.js"
"commanderjs/lib/**/*.js"
"express/lib/**/*.js"
"moment/src/lib/create/**/*.js"
"moment/src/lib/moment/**/*.js"
"lodash/.internal/equalArrays.js"
"lodash/hasPath.js"
"lodash/random.js"
"lodash/result.js"
"lodash/slice.js"
"lodash/split.js"
"lodash/toNumber.js"
"lodash/transform.js"
"lodash/truncate.js"
"lodash/unzip.js" )
#x=6

func1()
{
  incorporate=$1
  mode=$2
  i=$3

  for x in {0..19}; do
    if [[ "$x" == 5 ]]; then
      continue
    fi
    docker rm "${experiment_name}_${incorporate}_${mode}_${i}"
    docker run --name "${experiment_name}_${incorporate}_${mode}_${i}" --env time_per_target=${time} --env incorporate_execution_information=${incorporate} --env type_inference_mode=${mode} --env target_root_directory="./${benchmarks[$x]}" --env include="./${benchmark_files[$x]}" syntest/javascript:${experiment_name}
    docker cp "${experiment_name}_${incorporate}_${mode}_${i}:/app/syntest-javascript-benchmark/syntest" "./results/${experiment_name}-${time}-${incorporate}-${mode}-${benchmark_name[$x]}-${x}-${i}"
  done
}

mkdir results
mkdir log

for incorporate in "${incorporate_execution_information[@]}"; do
  for mode in "${modes[@]}"; do
    if [[ "$incorporate" == true && "$mode" == "none" ]]; then
      continue
    fi

    for i in {1..10}; do
      echo "running ${experiment_name} ex=${experiment_name} time=${time} inference=${incorporate} mode=${mode} trial ${i} for ${benchmark_name[$x]} with files ${benchmark_files[$x]}"
      func1 "$incorporate" "$mode" "$i" &> "log/log_${incorporate}_${mode}_${i}" &
   done
  done
done
