#!/usr/bin/env bash

# Copyright (c) 2021 AccelByte Inc. All Rights Reserved.
# This is licensed software from AccelByte Inc, for limitations
# and restrictions contact your company contract manager.
#
# Code generated. DO NOT EDIT!

# Meta:
# - random seed: 256
# - template file: python-cli-unit-test.j2

# Instructions:
# - Run the Justice SDK Mock Server first before running this script.

EXIT_CODE=0
PYTHON='python3'
MODULE='accelbyte_py_sdk_cli'
MODULE_PATH='../samples/cli'

export AB_BASE_URL="http://127.0.0.1:8080"
export AB_CLIENT_ID="admin"
export AB_CLIENT_SECRET="admin"
export AB_NAMESPACE="test"
export PYTHONPATH=$MODULE_PATH:$PYTHONPATH

touch "tmp.dat"

if [ "$BATCH" = true ] ; then

$PYTHON -m $MODULE 'start-interactive-session' --continue_on_error '--writer=tap' << END
dsmc-list-config --login_with_auth "Bearer foo"
dsmc-update-image '{"artifactPath": "FtBxyZcD", "image": "XBpGlsQu", "namespace": "Ju8vMf0I", "persistent": true, "version": "JkTrd8ID"}' --login_with_auth "Bearer foo"
dsmc-create-image '{"artifactPath": "cV2zXnTK", "dockerPath": "jXY1bPqa", "image": "miBxx9Cs", "namespace": "18EY84ek", "persistent": true, "version": "qRzHU1oh"}' --login_with_auth "Bearer foo"
dsmc-import-images 'tmp.dat' --login_with_auth "Bearer foo"
dsmc-create-image-patch '{"artifactPath": "570KQBVa", "dockerPath": "ewc72krS", "image": "ha68n3Yn", "namespace": "ozp1C2Km", "patchVersion": "IQTuBdNE", "persistent": true, "version": "xFb8CJ17"}' --login_with_auth "Bearer foo"
dsmc-get-config --login_with_auth "Bearer foo"
dsmc-create-config '{"claim_timeout": 76, "creation_timeout": 59, "default_version": "JZaMSxEC", "port": 2, "ports": {"Zbygyoar": 81}, "protocol": "RoeNHSb8", "providers": ["Rh3kgs9q"], "session_timeout": 33, "unreachable_timeout": 71}' --login_with_auth "Bearer foo"
dsmc-delete-config --login_with_auth "Bearer foo"
dsmc-update-config '{"claim_timeout": 2, "creation_timeout": 27, "default_version": "QsoBgiVp", "port": 82, "protocol": "8Cm3yvAS", "providers": ["UoxdxxFq"], "session_timeout": 24, "unreachable_timeout": 52}' --login_with_auth "Bearer foo"
dsmc-clear-cache --login_with_auth "Bearer foo"
dsmc-get-all-deployment --login_with_auth "Bearer foo"
dsmc-get-deployment 'GTJ8IEda' --login_with_auth "Bearer foo"
dsmc-create-deployment '{"allow_version_override": false, "buffer_count": 60, "buffer_percent": 38, "configuration": "p4w29KOu", "enable_region_overrides": false, "game_version": "19R6XDqW", "max_count": 67, "min_count": 20, "overrides": {"kP8npLEK": {"buffer_count": 76, "buffer_percent": 11, "configuration": "jiX7jpkV", "enable_region_overrides": false, "game_version": "3IaQYEmq", "max_count": 64, "min_count": 29, "name": "dOEGt9gP", "region_overrides": {"Oj0c6i0J": {"buffer_count": 21, "buffer_percent": 42, "max_count": 69, "min_count": 0, "name": "s73ucYnF", "use_buffer_percent": true}}, "regions": ["J3DK5T4E"], "use_buffer_percent": false}}, "region_overrides": {"gg0Y39Uo": {"buffer_count": 23, "buffer_percent": 31, "max_count": 43, "min_count": 3, "name": "VAgtsDhU", "use_buffer_percent": true}}, "regions": ["UscbQDjb"], "use_buffer_percent": true}' 'PMz2PTRl' --login_with_auth "Bearer foo"
dsmc-delete-deployment 'kyU89ZPO' --login_with_auth "Bearer foo"
dsmc-update-deployment '{"allow_version_override": true, "buffer_count": 50, "buffer_percent": 83, "configuration": "FJ42cwmz", "enable_region_overrides": true, "game_version": "BSMNcoAA", "max_count": 81, "min_count": 19, "regions": ["KNjfcYHm"], "use_buffer_percent": false}' 'YgBU1sqj' --login_with_auth "Bearer foo"
dsmc-create-root-region-override '{"buffer_count": 49, "buffer_percent": 72, "max_count": 99, "min_count": 66, "use_buffer_percent": false}' 'RSOFQBtu' '23REZ8hR' --login_with_auth "Bearer foo"
dsmc-delete-root-region-override 'VX7LGOvD' 'dYiQS9i7' --login_with_auth "Bearer foo"
dsmc-update-root-region-override '{"buffer_count": 24, "buffer_percent": 94, "max_count": 57, "min_count": 30, "use_buffer_percent": false}' 'G9gpxL6y' 'cTQdvln2' --login_with_auth "Bearer foo"
dsmc-create-deployment-override '{"buffer_count": 74, "buffer_percent": 52, "configuration": "uSQWEXL6", "enable_region_overrides": true, "game_version": "E1YHo9m1", "max_count": 96, "min_count": 4, "region_overrides": {"8hHtWvbN": {"buffer_count": 33, "buffer_percent": 12, "max_count": 92, "min_count": 33, "name": "slArFPiH", "use_buffer_percent": true}}, "regions": ["aCv8kU9d"], "use_buffer_percent": true}' 'BpdsJLhs' 'VyExrkxo' --login_with_auth "Bearer foo"
dsmc-delete-deployment-override 'ot0B7WOf' 'ercZdpMc' --login_with_auth "Bearer foo"
dsmc-update-deployment-override '{"buffer_count": 17, "buffer_percent": 58, "configuration": "s7YSfExa", "enable_region_overrides": true, "game_version": "zLteMbFA", "max_count": 23, "min_count": 39, "regions": ["4hr7HmOY"], "use_buffer_percent": false}' 'BA5ltAOX' 'mlG6eh1d' --login_with_auth "Bearer foo"
dsmc-create-override-region-override '{"buffer_count": 90, "buffer_percent": 6, "max_count": 29, "min_count": 91, "use_buffer_percent": true}' 'pBIcuC1d' 'QY93OJnJ' '6Te9vD8l' --login_with_auth "Bearer foo"
dsmc-delete-override-region-override 'dz7Hu8AD' '79kdWunv' 'izU0q1pH' --login_with_auth "Bearer foo"
dsmc-update-override-region-override '{"buffer_count": 49, "buffer_percent": 15, "max_count": 15, "min_count": 61, "use_buffer_percent": false}' 'GgdrysMi' 'zBGSRdP2' 'l7DNSZ8A' --login_with_auth "Bearer foo"
dsmc-get-all-pod-config '33' '98' --login_with_auth "Bearer foo"
dsmc-get-pod-config 'iPLQXSe0' --login_with_auth "Bearer foo"
dsmc-create-pod-config '{"cpu_limit": 7, "mem_limit": 6, "params": "OGTMlJjB"}' 'wj9HJHQK' --login_with_auth "Bearer foo"
dsmc-delete-pod-config 'seEdSXRD' --login_with_auth "Bearer foo"
dsmc-update-pod-config '{"cpu_limit": 89, "mem_limit": 43, "name": "guauw1xT", "params": "7eMwSl9M"}' 'LH0NnTJ2' --login_with_auth "Bearer foo"
dsmc-add-port '{"port": 41}' 'lNzBvwJa' --login_with_auth "Bearer foo"
dsmc-delete-port 'Qa547Jll' --login_with_auth "Bearer foo"
dsmc-update-port '{"name": "vA8RWSpa", "port": 2}' 'Ut7xk6Qx' --login_with_auth "Bearer foo"
dsmc-list-images --login_with_auth "Bearer foo"
dsmc-delete-image 'yWhfqoWf' 'Jw2o8oWU' --login_with_auth "Bearer foo"
dsmc-export-images --login_with_auth "Bearer foo"
dsmc-get-image-limit --login_with_auth "Bearer foo"
dsmc-delete-image-patch 'qvPCZ2Hz' 'T7NXmWDl' 'XsuNIdQJ' --login_with_auth "Bearer foo"
dsmc-get-image-detail 'R5lsNOlv' --login_with_auth "Bearer foo"
dsmc-get-image-patches 'kfwaSbns' --login_with_auth "Bearer foo"
dsmc-get-image-patch-detail 'uLCgToxu' 'VTekJgvg' --login_with_auth "Bearer foo"
dsmc-list-server --login_with_auth "Bearer foo"
dsmc-count-server --login_with_auth "Bearer foo"
dsmc-count-server-detailed --login_with_auth "Bearer foo"
dsmc-list-local-server --login_with_auth "Bearer foo"
dsmc-delete-local-server '6h5HIpH0' --login_with_auth "Bearer foo"
dsmc-get-server 'DviplEk4' --login_with_auth "Bearer foo"
dsmc-delete-server 'vj3LDp4y' --login_with_auth "Bearer foo"
dsmc-get-server-logs 'qDt8QUZD' --login_with_auth "Bearer foo"
dsmc-list-session --login_with_auth "Bearer foo"
dsmc-count-session --login_with_auth "Bearer foo"
dsmc-delete-session 'pxlHasin' --login_with_auth "Bearer foo"
dsmc-export-config-v1 --login_with_auth "Bearer foo"
dsmc-import-config-v1 --login_with_auth "Bearer foo"
dsmc-image-detail-client 'GcjrkmRM' --login_with_auth "Bearer foo"
dsmc-deregister-local-server '{"name": "ttgjDSaI"}' --login_with_auth "Bearer foo"
dsmc-register-local-server '{"custom_attribute": "VBmft3Ud", "ip": "g7p9PGmY", "name": "2H5kX4Ms", "port": 17}' --login_with_auth "Bearer foo"
dsmc-register-server '{"custom_attribute": "sSX28nAR", "pod_name": "xWRpv5ou"}' --login_with_auth "Bearer foo"
dsmc-shutdown-server '{"kill_me": true, "pod_name": "tvd28OUf"}' --login_with_auth "Bearer foo"
dsmc-get-server-session 'Ct8UJC5f' --login_with_auth "Bearer foo"
dsmc-create-session '{"client_version": "lNyj6HsT", "configuration": "tX8P3lln", "deployment": "aaS9lqyy", "game_mode": "gPcfkJIx", "matching_allies": [{"matching_parties": [{"party_attributes": {"fQZza8kN": {}}, "party_id": "VbDxVMq7", "party_members": [{"user_id": "HJk0F89x"}]}]}], "namespace": "Ac3YVfaE", "notification_payload": {}, "pod_name": "Ntrl0pTK", "region": "ZTXqzHuB", "session_id": "MYQSA2jz"}' --login_with_auth "Bearer foo"
dsmc-claim-server '{"session_id": "1ZOpdOjS"}' --login_with_auth "Bearer foo"
dsmc-get-session 'yMddB41J' --login_with_auth "Bearer foo"
dsmc-get-default-provider --login_with_auth "Bearer foo"
dsmc-list-providers --login_with_auth "Bearer foo"
dsmc-list-providers-by-region 'uMf7RUyB' --login_with_auth "Bearer foo"
dsmc-public-get-messages --login_with_auth "Bearer foo"
exit()
END

EXIT_CODE=$?

else

eval_tap() {
  if [ $1 -eq 0 ]; then
    echo "ok $2 - $3"
  else
    EXIT_CODE=1
    echo "not ok $2 - $3"
    sed 's/^/# /g' $4
  fi
  rm -f $4
}

echo "TAP version 13"
echo "1..68"

#- 1 Login
eval_tap 0 1 'Login # SKIP not tested' test.out
if [ $EXIT_CODE -ne 0 ]; then
  echo "Bail out! Login failed."
  exit $EXIT_CODE
fi

#- 2 ListConfig
$PYTHON -m $MODULE 'dsmc-list-config' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 2 'ListConfig' test.out

#- 3 SaveConfig
eval_tap 0 3 'SaveConfig # SKIP deprecated' test.out

#- 4 UpdateImage
$PYTHON -m $MODULE 'dsmc-update-image' \
    '{"artifactPath": "HRj8IiRi", "image": "mRllHT6D", "namespace": "c40vFFA6", "persistent": false, "version": "pU7EW3x1"}' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 4 'UpdateImage' test.out

#- 5 CreateImage
$PYTHON -m $MODULE 'dsmc-create-image' \
    '{"artifactPath": "dCpm55gO", "dockerPath": "eqQIqcJV", "image": "KmBM1J1I", "namespace": "buTrrkbm", "persistent": true, "version": "T1whOqmE"}' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 5 'CreateImage' test.out

#- 6 ImportImages
$PYTHON -m $MODULE 'dsmc-import-images' \
    'tmp.dat' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 6 'ImportImages' test.out

#- 7 CreateImagePatch
$PYTHON -m $MODULE 'dsmc-create-image-patch' \
    '{"artifactPath": "nDXIWrBP", "dockerPath": "lSay46mv", "image": "71BAZAOj", "namespace": "tFJ2vmTj", "patchVersion": "7tT7TZHW", "persistent": true, "version": "dCkIsZoA"}' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 7 'CreateImagePatch' test.out

#- 8 GetConfig
$PYTHON -m $MODULE 'dsmc-get-config' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 8 'GetConfig' test.out

#- 9 CreateConfig
$PYTHON -m $MODULE 'dsmc-create-config' \
    '{"claim_timeout": 34, "creation_timeout": 96, "default_version": "wPHcyFAd", "port": 52, "ports": {"tYciLIgR": 45}, "protocol": "FRr0gwB9", "providers": ["tz3vp99X"], "session_timeout": 94, "unreachable_timeout": 22}' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 9 'CreateConfig' test.out

#- 10 DeleteConfig
$PYTHON -m $MODULE 'dsmc-delete-config' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 10 'DeleteConfig' test.out

#- 11 UpdateConfig
$PYTHON -m $MODULE 'dsmc-update-config' \
    '{"claim_timeout": 94, "creation_timeout": 35, "default_version": "K3tE6n0s", "port": 25, "protocol": "ip1tw3L7", "providers": ["cUd9pqtv"], "session_timeout": 70, "unreachable_timeout": 11}' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 11 'UpdateConfig' test.out

#- 12 ClearCache
$PYTHON -m $MODULE 'dsmc-clear-cache' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 12 'ClearCache' test.out

#- 13 GetAllDeployment
$PYTHON -m $MODULE 'dsmc-get-all-deployment' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 13 'GetAllDeployment' test.out

#- 14 GetDeployment
$PYTHON -m $MODULE 'dsmc-get-deployment' \
    'PZwcCVOX' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 14 'GetDeployment' test.out

#- 15 CreateDeployment
$PYTHON -m $MODULE 'dsmc-create-deployment' \
    '{"allow_version_override": false, "buffer_count": 95, "buffer_percent": 1, "configuration": "80TmCwtD", "enable_region_overrides": false, "game_version": "AH01o6Nd", "max_count": 4, "min_count": 54, "overrides": {"IgzrDyWp": {"buffer_count": 62, "buffer_percent": 55, "configuration": "YGmmBawM", "enable_region_overrides": true, "game_version": "oKyNpdAa", "max_count": 36, "min_count": 24, "name": "8xwUfzOl", "region_overrides": {"QiZY4NbO": {"buffer_count": 84, "buffer_percent": 99, "max_count": 70, "min_count": 40, "name": "OTzNMvuq", "use_buffer_percent": true}}, "regions": ["Nl4CX4Ij"], "use_buffer_percent": false}}, "region_overrides": {"K4DEUJRV": {"buffer_count": 72, "buffer_percent": 22, "max_count": 60, "min_count": 3, "name": "0R1XRb0R", "use_buffer_percent": true}}, "regions": ["S1smeOln"], "use_buffer_percent": false}' \
    'rdTXCzaP' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 15 'CreateDeployment' test.out

#- 16 DeleteDeployment
$PYTHON -m $MODULE 'dsmc-delete-deployment' \
    'BtkZMio4' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 16 'DeleteDeployment' test.out

#- 17 UpdateDeployment
$PYTHON -m $MODULE 'dsmc-update-deployment' \
    '{"allow_version_override": true, "buffer_count": 5, "buffer_percent": 48, "configuration": "hloVS3rY", "enable_region_overrides": false, "game_version": "8QtcEmCE", "max_count": 95, "min_count": 4, "regions": ["75UfeypW"], "use_buffer_percent": false}' \
    'DNhzCL5s' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 17 'UpdateDeployment' test.out

#- 18 CreateRootRegionOverride
$PYTHON -m $MODULE 'dsmc-create-root-region-override' \
    '{"buffer_count": 97, "buffer_percent": 88, "max_count": 32, "min_count": 44, "use_buffer_percent": false}' \
    'EklkzLm8' \
    '8LpLuYRO' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 18 'CreateRootRegionOverride' test.out

#- 19 DeleteRootRegionOverride
$PYTHON -m $MODULE 'dsmc-delete-root-region-override' \
    '3C55yHpw' \
    'K2JaqenD' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 19 'DeleteRootRegionOverride' test.out

#- 20 UpdateRootRegionOverride
$PYTHON -m $MODULE 'dsmc-update-root-region-override' \
    '{"buffer_count": 64, "buffer_percent": 27, "max_count": 1, "min_count": 78, "use_buffer_percent": false}' \
    'lWiLjq06' \
    'n6a0rW8E' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 20 'UpdateRootRegionOverride' test.out

#- 21 CreateDeploymentOverride
$PYTHON -m $MODULE 'dsmc-create-deployment-override' \
    '{"buffer_count": 11, "buffer_percent": 20, "configuration": "paXtwYZJ", "enable_region_overrides": false, "game_version": "Q4WbwNms", "max_count": 62, "min_count": 8, "region_overrides": {"tjEurH8e": {"buffer_count": 22, "buffer_percent": 29, "max_count": 71, "min_count": 51, "name": "NKtRUaTz", "use_buffer_percent": true}}, "regions": ["Tdsmwzjk"], "use_buffer_percent": false}' \
    'n9oiQl05' \
    'g7cO3ZMb' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 21 'CreateDeploymentOverride' test.out

#- 22 DeleteDeploymentOverride
$PYTHON -m $MODULE 'dsmc-delete-deployment-override' \
    '6Ojlo6DM' \
    'NpP2qMrT' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 22 'DeleteDeploymentOverride' test.out

#- 23 UpdateDeploymentOverride
$PYTHON -m $MODULE 'dsmc-update-deployment-override' \
    '{"buffer_count": 84, "buffer_percent": 92, "configuration": "pjfU6wJh", "enable_region_overrides": true, "game_version": "1jOVkkUl", "max_count": 88, "min_count": 60, "regions": ["Z25Ia8uC"], "use_buffer_percent": false}' \
    'ZFlLtEVp' \
    'DAEbA82j' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 23 'UpdateDeploymentOverride' test.out

#- 24 CreateOverrideRegionOverride
$PYTHON -m $MODULE 'dsmc-create-override-region-override' \
    '{"buffer_count": 49, "buffer_percent": 23, "max_count": 32, "min_count": 30, "use_buffer_percent": true}' \
    'E5xRwh5b' \
    '45ebpcM7' \
    'ScSs3UOp' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 24 'CreateOverrideRegionOverride' test.out

#- 25 DeleteOverrideRegionOverride
$PYTHON -m $MODULE 'dsmc-delete-override-region-override' \
    'AwIp9rRt' \
    'n1PcCxdb' \
    'umeYgOdE' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 25 'DeleteOverrideRegionOverride' test.out

#- 26 UpdateOverrideRegionOverride
$PYTHON -m $MODULE 'dsmc-update-override-region-override' \
    '{"buffer_count": 55, "buffer_percent": 96, "max_count": 86, "min_count": 85, "use_buffer_percent": false}' \
    'W3KFfU8i' \
    'cH4081gR' \
    'B1GyLfLg' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 26 'UpdateOverrideRegionOverride' test.out

#- 27 GetAllPodConfig
$PYTHON -m $MODULE 'dsmc-get-all-pod-config' \
    '86' \
    '100' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 27 'GetAllPodConfig' test.out

#- 28 GetPodConfig
$PYTHON -m $MODULE 'dsmc-get-pod-config' \
    'uEbgUDEc' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 28 'GetPodConfig' test.out

#- 29 CreatePodConfig
$PYTHON -m $MODULE 'dsmc-create-pod-config' \
    '{"cpu_limit": 71, "mem_limit": 49, "params": "IvsPwOr0"}' \
    'BmV5iFvf' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 29 'CreatePodConfig' test.out

#- 30 DeletePodConfig
$PYTHON -m $MODULE 'dsmc-delete-pod-config' \
    'wFjTSmIE' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 30 'DeletePodConfig' test.out

#- 31 UpdatePodConfig
$PYTHON -m $MODULE 'dsmc-update-pod-config' \
    '{"cpu_limit": 32, "mem_limit": 28, "name": "LyLeUGmo", "params": "mGX9sXTZ"}' \
    '0v8pqLfc' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 31 'UpdatePodConfig' test.out

#- 32 AddPort
$PYTHON -m $MODULE 'dsmc-add-port' \
    '{"port": 89}' \
    'wGnReUUL' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 32 'AddPort' test.out

#- 33 DeletePort
$PYTHON -m $MODULE 'dsmc-delete-port' \
    'DX4QUIbb' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 33 'DeletePort' test.out

#- 34 UpdatePort
$PYTHON -m $MODULE 'dsmc-update-port' \
    '{"name": "5nh68Zny", "port": 92}' \
    'tRvW9hNB' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 34 'UpdatePort' test.out

#- 35 ListImages
$PYTHON -m $MODULE 'dsmc-list-images' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 35 'ListImages' test.out

#- 36 DeleteImage
$PYTHON -m $MODULE 'dsmc-delete-image' \
    'SFTtFrOm' \
    'jkFrFVA8' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 36 'DeleteImage' test.out

#- 37 ExportImages
$PYTHON -m $MODULE 'dsmc-export-images' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 37 'ExportImages' test.out

#- 38 GetImageLimit
$PYTHON -m $MODULE 'dsmc-get-image-limit' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 38 'GetImageLimit' test.out

#- 39 DeleteImagePatch
$PYTHON -m $MODULE 'dsmc-delete-image-patch' \
    't0xF34Xp' \
    't6ZlTTic' \
    '0kr2a0nI' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 39 'DeleteImagePatch' test.out

#- 40 GetImageDetail
$PYTHON -m $MODULE 'dsmc-get-image-detail' \
    '2oo7UHCJ' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 40 'GetImageDetail' test.out

#- 41 GetImagePatches
$PYTHON -m $MODULE 'dsmc-get-image-patches' \
    'K5sp0aCv' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 41 'GetImagePatches' test.out

#- 42 GetImagePatchDetail
$PYTHON -m $MODULE 'dsmc-get-image-patch-detail' \
    'Iq3aHVYI' \
    'lewLRuHY' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 42 'GetImagePatchDetail' test.out

#- 43 ListServer
$PYTHON -m $MODULE 'dsmc-list-server' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 43 'ListServer' test.out

#- 44 CountServer
$PYTHON -m $MODULE 'dsmc-count-server' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 44 'CountServer' test.out

#- 45 CountServerDetailed
$PYTHON -m $MODULE 'dsmc-count-server-detailed' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 45 'CountServerDetailed' test.out

#- 46 ListLocalServer
$PYTHON -m $MODULE 'dsmc-list-local-server' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 46 'ListLocalServer' test.out

#- 47 DeleteLocalServer
$PYTHON -m $MODULE 'dsmc-delete-local-server' \
    '83bGj0HT' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 47 'DeleteLocalServer' test.out

#- 48 GetServer
$PYTHON -m $MODULE 'dsmc-get-server' \
    'eeWXlIcR' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 48 'GetServer' test.out

#- 49 DeleteServer
$PYTHON -m $MODULE 'dsmc-delete-server' \
    'idqctDpy' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 49 'DeleteServer' test.out

#- 50 GetServerLogs
$PYTHON -m $MODULE 'dsmc-get-server-logs' \
    'gY0ax476' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 50 'GetServerLogs' test.out

#- 51 ListSession
$PYTHON -m $MODULE 'dsmc-list-session' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 51 'ListSession' test.out

#- 52 CountSession
$PYTHON -m $MODULE 'dsmc-count-session' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 52 'CountSession' test.out

#- 53 DeleteSession
$PYTHON -m $MODULE 'dsmc-delete-session' \
    'ED4MMO9T' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 53 'DeleteSession' test.out

#- 54 ExportConfigV1
$PYTHON -m $MODULE 'dsmc-export-config-v1' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 54 'ExportConfigV1' test.out

#- 55 ImportConfigV1
$PYTHON -m $MODULE 'dsmc-import-config-v1' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 55 'ImportConfigV1' test.out

#- 56 ImageDetailClient
$PYTHON -m $MODULE 'dsmc-image-detail-client' \
    'w2JH0qhW' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 56 'ImageDetailClient' test.out

#- 57 DeregisterLocalServer
$PYTHON -m $MODULE 'dsmc-deregister-local-server' \
    '{"name": "IwHWTgzJ"}' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 57 'DeregisterLocalServer' test.out

#- 58 RegisterLocalServer
$PYTHON -m $MODULE 'dsmc-register-local-server' \
    '{"custom_attribute": "FRYw6t1I", "ip": "KZLO6V4O", "name": "de46QmCi", "port": 7}' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 58 'RegisterLocalServer' test.out

#- 59 RegisterServer
$PYTHON -m $MODULE 'dsmc-register-server' \
    '{"custom_attribute": "gdpP7RTC", "pod_name": "587lmUmB"}' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 59 'RegisterServer' test.out

#- 60 ShutdownServer
$PYTHON -m $MODULE 'dsmc-shutdown-server' \
    '{"kill_me": true, "pod_name": "iPZBnpOf"}' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 60 'ShutdownServer' test.out

#- 61 GetServerSession
$PYTHON -m $MODULE 'dsmc-get-server-session' \
    'kllxfq0N' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 61 'GetServerSession' test.out

#- 62 CreateSession
$PYTHON -m $MODULE 'dsmc-create-session' \
    '{"client_version": "srSjw5Ho", "configuration": "g0blM1d5", "deployment": "MStYGczL", "game_mode": "INlEC0OE", "matching_allies": [{"matching_parties": [{"party_attributes": {"sE3yzIsU": {}}, "party_id": "P0NjluOr", "party_members": [{"user_id": "GZTzsLW7"}]}]}], "namespace": "Fjfs9nIk", "notification_payload": {}, "pod_name": "cZ38fUEa", "region": "njKHbXfk", "session_id": "1zxdzxg0"}' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 62 'CreateSession' test.out

#- 63 ClaimServer
$PYTHON -m $MODULE 'dsmc-claim-server' \
    '{"session_id": "UXcRyHi3"}' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 63 'ClaimServer' test.out

#- 64 GetSession
$PYTHON -m $MODULE 'dsmc-get-session' \
    'u8BzVWu1' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 64 'GetSession' test.out

#- 65 GetDefaultProvider
$PYTHON -m $MODULE 'dsmc-get-default-provider' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 65 'GetDefaultProvider' test.out

#- 66 ListProviders
$PYTHON -m $MODULE 'dsmc-list-providers' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 66 'ListProviders' test.out

#- 67 ListProvidersByRegion
$PYTHON -m $MODULE 'dsmc-list-providers-by-region' \
    'tOmhUtCg' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 67 'ListProvidersByRegion' test.out

#- 68 PublicGetMessages
$PYTHON -m $MODULE 'dsmc-public-get-messages' \
    --login_with_auth "Bearer foo" \
    > test.out 2>&1
eval_tap $? 68 'PublicGetMessages' test.out


fi

rm -f "tmp.dat"

exit $EXIT_CODE
