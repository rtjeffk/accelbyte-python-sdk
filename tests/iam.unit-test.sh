#!/usr/bin/env bash
set -e
set -o pipefail
set -x
export AB_BASE_URL="http://localhost:8080"
export AB_CLIENT_ID="admin"
export AB_CLIENT_SECRET="admin"
export AB_NAMESPACE="namespace"
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-bans-type' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-list-ban-reason' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-client' 'vheNmitnZyGV' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-update-client' '{"ClientName":"qcoYWlWCWXka","RedirectUri":"zNgcmpMFnCDi"}' 'PpkiUGlAiBFb' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-update-client-permission' '{"Permissions":[{"Action":899,"Resource":"tVdbZdfzjKKD"}]}' 'OAidNyyXHVLq' '--login_as' 'client'
#'python3' '-m' 'accelbyte_py_sdk' 'iam-add-client-permission' 'JPZGVijoKkCg' 'TzuvGiZVmuPb' '100' '--login_as' 'client'
#'python3' '-m' 'accelbyte_py_sdk' 'iam-delete-client-permission' 'NutEIreNPzyB' 'EchUxvgFrvby' '52' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-update-client-secret' '{"NewSecret":"hrKUSZGONjUJ"}' 'NbAvHfhYEQQo' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-clientsby-namespace' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-create-client-by-namespace' '{"ClientId":"adc083a664ae3708135da13fb6d7bacb","ClientName":"sBSAvWRRPrhC","ClientPermissions":[{"Action":228,"Resource":"cWasszOPvUxA","SchedAction":315,"SchedCron":"HmyyWboaqzex","SchedRange":["EhDBpyiyHObd"]}],"Namespace":"AgedBamboozledElephant2F22EF","RedirectUri":"GKsVFmGsCvCE","Secret":"WMwLmaSPAFYF"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-delete-client-by-namespace' 'hvBnTjpEeLqH' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-create-user' '{"AuthType":"BjKLwyEjwSnw","Country":"GB","DisplayName":"ClamorousEnviousCarp3B8AC0","LoginId":"azqJCyLSxDCN","Password":"g`jdZwBq6r7(D-kC","PasswordMD5Sum":"ytqRfJntsqmH"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-admin-users-by-role-id' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-user-by-login-id' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-user-by-platform-user-id' 'qvBAuPUsyqWn' 'PgKYQGoTWxgx' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-forgot-password' '{"Context":"ICUJDXqfkLyn","LanguageTag":"JkViPOvrgmqT","LoginID":"hfVyNrfyByUe"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-users-by-login-ids' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-reset-password' '{"Code":"DiCwwRVBtjAb","LoginID":"WSQVqNHDdbrm","NewPassword":"pgnAitRSJzVr"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-user-by-user-id' 'ALdkYhQDSrRL' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-update-user' '{"Country":"IE","DateOfBirth":"YJpOKrGDFobh","DisplayName":"DeviousEnergeticChipmunkECC4CF","LanguageTag":"QViUotjcTVDG"}' 'UlNpEntDkQdE' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-delete-user' 'qBOYRKrfvsJc' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-ban-user' '{"ban":"umgsAJkMHXuc","comment":"YmCtdJooAOEK","endDate":"mcIgzjOKBcxk","reason":"fmybosaRXFcv","skipNotif":false}' 'sTjygPeFkPVm' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-user-ban-history' 'FhdWYhZirBGk' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-disable-user-ban' 'JtlXXxAKhGdG' 'WfWsAjIuJvEM' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-enable-user-ban' 'vAAQslKMaTck' 'KGfEkHJJRbzq' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-user-information' 'uegZUqfVNyzK' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-delete-user-information' 'cSpvMzTZwEIc' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-user-login-histories' 'iXAlSeIujjrI' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-save-user-permission' '{"Permissions":[{"Action":705,"Resource":"fswVbRtjTNeK","SchedAction":350,"SchedCron":"vUpLVScJIcnp","SchedRange":["wxLbAxIsZNHG"]}]}' 'ycdEchfUiwgW' '--login_as' 'client'
#'python3' '-m' 'accelbyte_py_sdk' 'iam-add-user-permission' '{"SchedAction":425,"SchedCron":"qbzBxipHOgsY","SchedRange":["STtLGYyLrwdu"]}' 'RvyfnRYXSMFj' 'FvmJwOkFtSzY' '4' '--login_as' 'client'
#'python3' '-m' 'accelbyte_py_sdk' 'iam-delete-user-permission' 'FYXkUBLNLuMZ' 'UdWFGGewNEEF' '25' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-user-platform-accounts' 'EfAmTvfuTets' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-user-mapping' 'EPnjcRPgPDki' 'OUoXXyBcbwxe' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-platform-link' 'WAdxfeSVPytw' 'YWpXEtkmFyqv' 'TwpkXpLTFYDz' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-platform-unlink' 'PCaObgptKmlc' 'tacTEFcHvuSk' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-publisher-user' 'DWVyhSPNeBhK' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-save-user-roles' '["MpyixiWmcTGH"]' 'nsNGHsHlsvLL' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-add-user-role' 'ftRcYJFBjZTd' 'tkSfvKIwsubX' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-delete-user-role' 'yduYPejSmLcn' 'rpOuxRpUhcgY' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-upgrade-headless-account' '{"LoginID":"yPotOeuFPAvz","Password":"HkU:W-hpd{FMq+,K"}' 'bywWWoASkwpQ' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-upgrade-headless-account-with-verification-code' '{"Code":"mdyrHfGIQcKt","Password":"qv =XyphCY2&#+,y","loginId":"SELZaoLQbkAS"}' 'yTtFKHQurAlC' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-user-verification' '{"Code":"OzaGyItcQYwl","ContactType":"xWkEhXeYmHvR","LanguageTag":"CAIdwIcaVZLx"}' 'iSNRZedjIxsB' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-send-verification-code' '{"Context":"EmMfYRbOJSdW","LanguageTag":"kzuQPGNCHfbz","LoginID":"FGUYsuLyaHiY"}' 'scrQvjjxxurE' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-authorization' 'NeZwWCddsRVW' 'ZwWWgYqlxSzg' 'token' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-jwks' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-revoke-user' 'dbDNHqlfzDWt' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-revocation-list' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-token-grant' 'refresh_token' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-verify-token' 'VbpOeFGFhxBY' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-roles' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-create-role' '{"AdminRole":true,"Managers":[{"DisplayName":"AuthenticAmbidextrousAardvarkEF99AF","Namespace":"AbdicatedElasticCarpFEDED2","UserId":"8086bef49d80dec5f4fcc9f87cfae8c2"}],"Members":[{"DisplayName":"DraconicDraconicDodo66D54A","Namespace":"BlasphemousAbdicatedElephant6FB7AA","UserId":"fc3b5aa83efb8d70e495fb3dda11cf2c"}],"Permissions":[{"Action":516,"Resource":"PszzYQygksLz","SchedAction":243,"SchedCron":"UfWulQnmxgSe","SchedRange":["WONkFvbsXGrF"]}],"RoleName":"wiwuonJfDAHu"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-role' 'rGyDOzPBaVld' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-update-role' '{"RoleName":"TSqzhDYVsDSK"}' 'OPhjgIOTdcNA' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-delete-role' 'DaHWJiBRgCVR' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-role-admin-status' 'pUOzNFvitTLn' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-set-role-as-admin' 'tGBXpWjqHKmM' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-remove-role-admin' 'kfYPfTSapWjc' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-role-managers' 'hxYCUaAWtRIa' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-add-role-managers' '{"Managers":[{"DisplayName":"CagedArchaicAntelope030C88","Namespace":"BoisterousEnviousBaboonB74EEA","UserId":"ac457addc511eb8e4d43d41bca07b5a6"}]}' 'uXsCOywfrqZx' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-remove-role-managers' '{"Managers":[{"DisplayName":"EnhancedBoisterousAardvark1C11CE","Namespace":"AthleticAgedAardvarkBCF9D2","UserId":"dee3ee79ef6c4ff6603e633c89af6d96"}]}' 'HKAnflVRfpwk' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-role-members' 'prEDNgfWBixo' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-add-role-members' '{"Members":[{"DisplayName":"BumptiousEnhancedAxolotlCDB3AB","Namespace":"BemusedBallisticDeerEAD6B0","UserId":"ebfbb0fceaedc809fef69028fdff6aaa"}]}' 'mrhlPHMYHqJy' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-remove-role-members' '{"Members":[{"DisplayName":"AmbidextrousBemusedAardvarkEBFE6B","Namespace":"ArchaicCarnivorousEmuF88DBD","UserId":"775dfbcc9f21e6511d9ac51cfd6452ea"}]}' 'rmDdghcBgstn' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-update-role-permissions' '{"Permissions":[{"Action":430,"Resource":"JIILFbyBTsTy","SchedAction":253,"SchedCron":"lYvEnxuiRRSh","SchedRange":["xFDwfysTPTvi"]}]}' 'iiardQENgBuz' '--login_as' 'client'
#'python3' '-m' 'accelbyte_py_sdk' 'iam-add-role-permission' '{"SchedAction":240,"SchedCron":"idTOAMtZixHO","SchedRange":["fWhpPGXyrDHc"]}' 'GFEVFuuKcbPv' 'LsEJxCXBzChG' '10' '--login_as' 'client'
#'python3' '-m' 'accelbyte_py_sdk' 'iam-delete-role-permission' 'HnYoUrtnEoFN' 'DuHbEdlrUBmP' '51' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-age-restriction-status-v2' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-update-age-restriction-config-v2' '{"AgeRestriction":589,"Enable":true}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-list-country-age-restriction' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-update-country-age-restriction' '{"AgeRestriction":833}' 'nLjzgxlUnsLk' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-search-users-v2' 'XdiAkHrMqGBe' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-user-by-user-id-v2' 'RKLpWQucASLE' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-update-user-v2' '{"Country":"IE","DateOfBirth":"ByyWrocSddtV","DisplayName":"DraconicAmphibiousElephantCA3ACA","LanguageTag":"oeOTCclzEDVz"}' 'FuBeEuLHfedV' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-ban-user-v2' '{"ban":"mBxsxwxQXIVP","comment":"brWFSfSBqGsW","endDate":"DLoUWLFIMQFF","reason":"eAIxtgYGOyPs","skipNotif":false}' 'SVFxZdAdGpkI' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-user-ban-v2' 'cNLnmtcmviev' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-disable-user-v2' '{"Reason":"DRSVHrwXxXqc"}' 'STnLlCiRFbuH' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-enable-user-v2' 'JfKWRGgbzKZu' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-reset-password-v2' '{"LanguageTag":"KYhHmjouFWPi","NewPassword":"GqQMrMwwsdZS","OldPassword":"TerHooNeHaHH"}' 'tnnfvhdqHJTg' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-delete-platform-link-v2' 'kGHSSdAHlfvw' 'ahKQmGaQErnY' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-put-user-roles-v2' '["qEsGYezQiIwy"]' 'UOOWAWALRbjQ' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-create-user-roles-v2' '["FsrJPbJYZiOA"]' 'INTSUDoLPQsA' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-create-user-v2' '{"AuthType":"iFrPBuPPWBZT","Country":"CN","DisplayName":"AgedAmphibiousEmu95463F","LoginId":"pjzcyZfktlmj","Password":"qBD.)u>A%<p(h%33","PasswordMD5Sum":"yCAicQhgxKTn"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-forgot-password-v2' '{"Context":"ZAFzJhMzMudg","LanguageTag":"adjGiYOpxvKR","LoginID":"sJhUkaflJHnK"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-reset-password-v2' '{"Code":"aiHFVnzTzwNf","LoginID":"ieOYedlGqjcT","NewPassword":"CpAyvoECUGGI"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-get-user-by-user-idv2' 'QAFBKwnAsQLY' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-update-user-v2' '{"Country":"RU","DateOfBirth":"rJmcmcOayyml","DisplayName":"DangerousBemusedDodo59198C","LanguageTag":"KqlIWzxzEhZS"}' 'SzkvZFQFivYz' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-get-user-ban' 'VzbQIYYQKgJY' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-update-password-v2' '{"LanguageTag":"nBbfKVrVrBNN","NewPassword":"omycOFykbtpr","OldPassword":"gvgdsaOcylEq"}' 'jpPFpckrGjAy' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-list-justice-platform-accounts' 'qVsSKiWkupRc' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-platform-link-v2' 'ViqLqOgoJmgo' 'brLcQktxtZAN' 'wgBQeXMakpkN' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-delete-platform-link-v2' 'VZPYlnLxBqqs' 'RyUrmnLluplA' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-bans-type-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-list-ban-reason-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-list-admins-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-age-restriction-status-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-update-age-restriction-config-v3' '{"ageRestriction":315,"enable":true}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-list-country-age-restriction-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-update-country-age-restriction-v3' '{"ageRestriction":559}' 'DOUGZRXpWOre' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-banned-users-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-bans-type-with-namespace-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-clients-by-namespace-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-create-client-v3' '{"audiences":["aceuEvbjPFiA"],"baseUri":"WEAdUqbUWSbX","clientId":"76edad1f7b713aa4b37b727d6a88f182","clientName":"oQdmjzlSrlEL","clientPermissions":[{"action":761,"resource":"BbmXLXqgtvfg","schedAction":941,"schedCron":"VpZVbQBDiPUB","schedRange":["GEoBrGxwWVvw"]}],"namespace":"ConfinedDangerousCamelF1363B","oauthClientType":"MvVXeeZjeINu","redirectUri":"UfnemRpjWCWf","secret":"GFGHasysfDoN"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-clientsby-namespaceby-idv3' 'JCdUVJeKPkBu' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-delete-client-v3' 'QjwVbhHSJwQh' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-update-client-v3' '{"audiences":["cxGgNvgFzrLy"],"baseUri":"FmIZlGUaPAUb","clientName":"awHhahxmrLXn","clientPermissions":[{"action":119,"resource":"WCQVuckTZNcG","schedAction":516,"schedCron":"gdIiPWHeKqUh","schedRange":["ohbFnbUMdFAX"]}],"namespace":"DexterousBemusedDodo540059","redirectUri":"NWJBtiQCJSNF"}' 'hoBhwfgXyMVq' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-update-client-permission-v3' '{"permissions":[{"action":372,"resource":"vRXuSRlYEMuy"}]}' 'BnSroFxXvrWI' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-add-client-permissions-v3' '{"permissions":[{"action":577,"resource":"qcQgUnuMXTmc"}]}' 'eJuQcWkfOKEn' '--login_as' 'client'
#'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-delete-client-permission-v3' 'IrLhoJWLPDVh' 'KyaFbiuePIYr' '69' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-retrieve-all-third-party-login-platform-credential-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-retrieve-all-active-third-party-login-platform-credential-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-retrieve-all-sso-login-platform-credential-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-retrieve-third-party-login-platform-credential-v3' 'BxOySFrNqzFO' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-add-third-party-login-platform-credential-v3' '{"ACSURL":"AoFhsFhypkoV","AWSCognitoRegion":"KhRWiCDFZzCN","AWSCognitoUserPool":"VyJtYSkFdCEA","AppId":"f5c5f93afb66dea03aa21c75a3ea5235","ClientId":"009ddf23ada6c867c6a076f84b41b2ab","Environment":"HeVIhJRxsJzT","FederationMetadataURL":"https://www.example.com/UruGSudnDi","IsActive":true,"OrganizationId":"EUThlvzuCTAY","RedirectUri":"otFXihZDuLxf","Secret":"ZWVtBpUAmSvB"}' 'BLRmciQiKnfl' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-delete-third-party-login-platform-credential-v3' 'ptIYkwoLRGlz' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-update-third-party-login-platform-credential-v3' '{"ACSURL":"HOGsJvnwetXh","AWSCognitoRegion":"XcaVSZkqcxJz","AWSCognitoUserPool":"gGIpFSwyhnmF","AppId":"5bfe5a6a64d306e14133ac87dcaaa3ec","ClientId":"8cbff37635cd45d742ecc2ddd4aa7a0f","Environment":"CSVTPfdawDMr","FederationMetadataURL":"https://www.example.com/jSqDawiXPC","IsActive":false,"OrganizationId":"cAbbGBoedMSA","RedirectUri":"gFHmoBvRFIGy","Secret":"amYgrtMrCmmd"}' 'sngtdCalRYnj' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-retrieve-sso-login-platform-credential' 'pKKWVAVasjgd' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-add-sso-login-platform-credential' '{"acsUrl":"https://www.example.com/aMYjGZsXAb","apiKey":"KnNFgEpATMMb","appId":"af56c76cffb8253dabc8a27abecbf9da","federationMetadataUrl":"https://www.example.com/aKigIBNvOq","isActive":false,"redirectUri":"CpugiuoHQaCk","secret":"hbELJmOMpsOc","ssoUrl":"https://www.example.com/wxcdjRNJeR"}' 'eIrQOzvBKgkZ' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-delete-sso-login-platform-credential-v3' 'pArujrVZloQa' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-update-sso-platform-credential' '{"acsUrl":"https://www.example.com/pKuycGgMPy","apiKey":"rTcvNVjtskkS","appId":"30e8df584774aedffbcbfad4dcfbeeb1","federationMetadataUrl":"https://www.example.com/YKNfKFFNVQ","isActive":true,"redirectUri":"bkFIkfqBGQyr","secret":"cPOnJSrcqWmu","ssoUrl":"https://www.example.com/ApMeGDzLTo"}' 'edCxCfJnwGQU' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-admin-users-by-role-id-v3' 'xAGJsvKJpSEp' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-user-by-email-address-v3' '--login_as' 'client'
#'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-invite-user-v3' '{"emailAddresses":["IkMFVvOsHOzw"],"roles":["zzjkEnVwplHN"]}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-list-users-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-search-user-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-bulk-user-by-email-address-v3' '{"listEmailAddressRequest":["cxzUcKsKJdFv"]}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-user-by-user-id-v3' 'wbUEoWaPvfAT' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-update-user-v3' '{"country":"CA","dateOfBirth":"eMEmBXFkWMOi","displayName":"AbandonedDraconicAardvark05BA73","languageTag":"JQKVjfYixaOA","userName":"AmbidextrousBasicCarp8ACD7A"}' 'VYZBxcTfIHVy' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-user-ban-v3' 'axCvregPiNHj' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-ban-user-v3' '{"ban":"QyNmTlbDEwdu","comment":"QsbRtsGkQaYn","endDate":"aDZfzUjChOnH","reason":"DqkJJBtewsAU","skipNotif":true}' 'hYkEMHlyuWJg' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-update-user-ban-v3' '{"enabled":true,"skipNotif":true}' 'PbdnQmotDRkM' 'VBtMgmKdBfFQ' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-send-verification-code-v3' '{"context":"zaCDwYPkRZrx","emailAddress":"ENHANCEDCARP+F3098E@fakemail.com","languageTag":"SusEITFMHxZx"}' 'sMjauVlszSlu' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-verify-account-v3' '{"Code":"sebjLmLtEXbQ","ContactType":"yZvQOsuccfbn","LanguageTag":"cPTPWqHaySWe"}' 'nmzyIOoddhpF' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-user-verification-code' 'mMbAoTrKwsjm' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-user-deletion-status-v3' 'UBNeRPVpXZfv' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-update-user-deletion-status-v3' '{"enabled":false}' 'rXQOHqEtykvv' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-upgrade-headless-account-v3' '{"code":"HtqSOJQesmRw","country":"RU","dateOfBirth":"ojNLvhLWCxgB","displayName":"AutonomousEnergeticDodoCD0DB0","emailAddress":"DEFAMEDDODO+8CBCD7@fakemail.com","password":"PS)V-P?JQ3E;1aPA"}' 'rHqbgqXezVDI' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-delete-user-information-v3' 'djaiGGuiJygE' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-user-login-histories-v3' 'LmDceLsQmUOO' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-update-user-permission-v3' '{"Permissions":[{"Action":115,"Resource":"cpHnPdMawRoA","SchedAction":138,"SchedCron":"VaBjKllUQWdC","SchedRange":["yOVbWqNgxEJN"]}]}' 'xvNoxHeQMpdZ' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-add-user-permissions-v3' '{"Permissions":[{"Action":315,"Resource":"pgLtDLIyXaLk","SchedAction":947,"SchedCron":"FNiXfVlYAfca","SchedRange":["oIloPqorpYcm"]}]}' 'zegKOXhwDAve' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-delete-user-permission-bulk-v3' '[{"Action":820,"Resource":"YoUdTOPUjyuT"}]' 'GGqplWsOLwVw' '--login_as' 'client'
#'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-delete-user-permission-v3' 'XuAtxEkKbdVP' 'FfCDramWMYjJ' '97' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-user-platform-accounts-v3' 'nLxBKIDHarjp' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-create-justice-user' 'EIxGZRLKqnJz' 'ISiAchLUYyuJ' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-link-platform-account' '{"platformId":"wFwEvCCGnxPh","platformUserId":"shcERfoZXrzE"}' 'glFUVzTNEKGG' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-platform-unlink-v3' '{"platformNamespace":"EgregiousCarnivorousBeetleB949DB"}' 'nVLCxduTSLMR' 'pPCChWTktSCw' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-platform-link-v3' 'bhYBpXStzdUS' 'LWeHJLPDxVTT' 'GulHNTLzSaGV' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-delete-user-roles-v3' '["qCnvMktJwysc"]' 'ZdqHhuxzeSQi' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-save-user-role-v3' '[{"namespace":"CubicEditedCarpB6AE4E","roleId":"b9638e95128bdcda33b8155ffb5fd14b"}]' 'gnPCSTyLDgrJ' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-add-user-role-v3' 'rQGfQSrNuoww' 'KXGzOQXCTUrV' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-delete-user-role-v3' 'dfIpSefWeFRW' 'WKGjsoXBmqFK' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-update-user-status-v3' '{"enabled":false,"reason":"anNWAretlyHk"}' 'rQFSHJzTfgmA' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-verify-user-without-verification-code-v3' 'GgcNqUnZYQVh' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-roles-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-create-role-v3' '{"adminRole":false,"isWildcard":false,"managers":[{"displayName":"AmphibiousEnhancedElephantF7C85C","namespace":"CubicBallisticBeetle90FF8D","userId":"d6ab1cac0ba8ac128d4aaee8a6f3bd42"}],"members":[{"displayName":"EnragedAuthenticElephantBF2C1D","namespace":"BionicBallisticAardvark5A0862","userId":"fd9e4beac3bfa63fa13f4fb0cc7a61da"}],"permissions":[{"action":71,"resource":"TjGcJGrEUsAC","schedAction":860,"schedCron":"wsLLgkoSHOmK","schedRange":["qcChpQpHxeWI"]}],"roleName":"xIDkJdNqLToF"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-role-v3' 'JjhGrRWdMtUc' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-delete-role-v3' 'uiNufheAOlef' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-update-role-v3' '{"isWildcard":false,"roleName":"qkVBxOExziUx"}' 'pjSsIcRSjyfM' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-role-admin-status-v3' 'PnQbUJEWcowU' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-update-admin-role-status-v3' 'pvUaeklNskqW' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-remove-role-admin-v3' 'nRTMKGOlNGtJ' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-role-managers-v3' 'WXyXnqHCHpvz' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-add-role-managers-v3' '{"managers":[{"displayName":"EnragedCarnivorousElephantAB2813","namespace":"CagedBionicAntelopeF386BB","userId":"04edc9c97adf157974acf502eafd91da"}]}' 'AVIliYeXIOtD' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-remove-role-managers-v3' '{"managers":[{"displayName":"ChargedEnhancedDingo4B9CAC","namespace":"BemusedEnragedCamel798F6E","userId":"b414de6b8e0dc440b0b75daf179b4afc"}]}' 'fgBTlQWBjhAW' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-role-members-v3' 'yUaKxtzGvWog' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-add-role-members-v3' '{"members":[{"displayName":"ArchaicAuthenticCarp60C71A","namespace":"ElasticDemocraticDingoF526FC","userId":"0f7a575af174fbca8c13d0c8d32f31db"}]}' 'LlVFumdyxrCd' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-remove-role-members-v3' '{"members":[{"displayName":"CarnivorousDemonicCarpCBFEDA","namespace":"AmphibiousBemusedBaboonB7BAA8","userId":"ac2cdcda0ebcd6eededc8b4fed8aa0dd"}]}' 'RAWOJRpoiAtq' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-update-role-permissions-v3' '{"permissions":[{"action":198,"resource":"PrFbjqqvztEm","schedAction":313,"schedCron":"mklvpGxqTBDx","schedRange":["HXXqaHEScuwc"]}]}' 'KPAWUbCZWeNO' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-add-role-permissions-v3' '{"permissions":[{"action":275,"resource":"rPZVozJbsFLC","schedAction":35,"schedCron":"dtGyUiSIanMA","schedRange":["mYoWYcMKgsCo"]}]}' 'CEFLFfjQzWvn' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-delete-role-permissions-v3' '["lRmgthzvadnK"]' 'mYYGdTDHabji' '--login_as' 'client'
#'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-delete-role-permission-v3' 'lYvWMnaMGlik' 'aNqKynchztWL' '95' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-my-user-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-user-authentication-v3' 'JXQSmiVRgyvl' 'pKSRvaPPlpDz' 'ITamALIwdszr' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-country-location-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-logout' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-revoke-user-v3' 'sNHbMGvOiSSu' '--login_as' 'client'
#'python3' '-m' 'accelbyte_py_sdk' 'iam-authorize-v3' 'code' 'aSWnFmWjeJwx' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-token-introspection-v3' 'VVAzmOIyLcvD' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-jwksv3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-retrieve-user-third-party-platform-token-v3' 'FEzPDSPmoSoE' 'NWMQzCBFhWvz' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-auth-code-request-v3' 'BuOPuoEwBpmz' 'IpLRKNNIyPfY' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-platform-token-grant-v3' 'BmnNJXiQWxrp' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-revocation-list-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-token-revocation-v3' 'PKKXyMWIPyyW' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-token-grant-v3' 'client_credentials' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-platform-authentication-v3' 'ZtuXXAIwUAGr' 'LVAiGauWmfzb' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-retrieve-all-active-third-party-login-platform-credential-public-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-list-user-id-by-platform-user-i-ds-v3' '{"platformUserIds":["jXjFvCqIcKAF"]}' 'HMAnJfkpJQFl' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-get-user-by-platform-user-idv3' 'rUPNxbJtRJEM' 'ONKttsHvIkYc' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-get-async-status' 'ByZcpLIxZILV' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-search-user-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-create-user-v3' '{"PasswordMD5Sum":"OQORbzfmUiIS","acceptedPolicies":[{"isAccepted":false,"localizedPolicyVersionId":"DpYjksWCnoMf","policyId":"HNemZLzGVCKS","policyVersionId":"mpawSIJiJCVT"}],"authType":"HtmcwdngsdKI","country":"CN","dateOfBirth":"dWrchMCbVTBI","displayName":"CaloricEnviousElephantAA1BBC","emailAddress":"BEMUSEDAPPLE+F6AA6D@fakemail.com","password":"a&kQuKbHuH<<gF9}"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-forgot-password-v3' '{"emailAddress":"BASICETROG+6BC331@fakemail.com","languageTag":"GmvwsekVrjnD"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-get-admin-invitation-v3' 'gVzpoNUvTiEF' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-create-user-from-invitation-v3' '{"authType":"vTUyWNwNlmtl","country":"CN","dateOfBirth":"oOwgnYoqRzRA","displayName":"ClimaticAmphibiousDodoCB6766","password":"RR1ZI@9sL7V8<gG0"}' 'kYRktPLPyqAE' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-update-user-v3' '{"country":"ID","dateOfBirth":"PqBwDijYndWi","displayName":"DexterousCubicEmu8AD7DD","languageTag":"boKCGWgdkaDa","userName":"DangerousAgedAardvarkA5C6EA"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-update-user-v3' '{"country":"PH","dateOfBirth":"eWfKjEXdzxQh","displayName":"BamboozledBionicAardvark2FB65B","languageTag":"pUTingMlUPBL","userName":"EnragedDefamedElephant2B1C17"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-send-verification-code-v3' '{"context":"AFJPpJIMCsqb","emailAddress":"BROKENAXOLOTL+6DDE6C@fakemail.com","languageTag":"vfTcVLmgfTOl"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-user-verification-v3' '{"code":"iReXVeHWZbFo","contactType":"JdnpzagxKXOk","languageTag":"hWIEHVbRYwgz"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-upgrade-headless-account-v3' '{"code":"MYzqwmCzpHrp","country":"ID","dateOfBirth":"GFuuALzPvWjk","displayName":"BemusedAbdicatedAntelopeE9425E","emailAddress":"AGEDBLUEBERRY+3FEF14@fakemail.com","password":"rM@i5FrW7R9sCQIj"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-verify-headless-account-v3' '{"emailAddress":"AMPHIBIOUSAPPLE+ABFDFF@fakemail.com","password":"tg0XfKrRE.=Jn#sl"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-update-password-v3' '{"languageTag":"pbhHmWjtmAZM","newPassword":"YrJegrwLKkIZ","oldPassword":"PLVFrNUCAvsW"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-create-justice-user' 'GvlSijeRqMmW' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-platform-link-v3' 'ksZIpRUBcpsU' 'vacVLFnIhVQY' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-platform-unlink-v3' '{"platformNamespace":"ChargedEnviousAardvarkE1C13F"}' 'LuaYTpqLWKsw' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-web-link-platform' 'lUquQGEkvUad' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-web-link-platform-establish' 'obqTdWecsZGX' 'jLREEiAOtXXa' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-reset-password-v3' '{"code":"mfjeEWpNttrU","emailAddress":"ECCENTRICBABOON+16840A@fakemail.com","newPassword":"mijbBNdIexif"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-get-user-by-user-id-v3' 'mICmiJIoNdgP' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-get-user-ban-history-v3' 'zXjkCYjtvzke' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-get-user-login-histories-v3' 'AipUCFZolEea' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-get-user-platform-accounts-v3' 'dsNMrOPghRkX' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-link-platform-account' '{"platformId":"mcExOQjTNrOY","platformUserId":"UESIbJYKyDLD"}' 'UGpxSPvyYWXi' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-validate-user-by-user-id-and-password-v3' 'edlIiQjcQmEq' 'fdYrWxRGXUjN' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-get-roles-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-get-role-v3' 'uHtDWeyokUDf' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-get-my-user-v3' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-platform-authenticate-samlv3-handler' 'APrIMQQlElrS' 'iTGkUObMjAav' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-login-sso-client' 'qSffQWzexqRU' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-logout-sso-client' 'rBVgEtvwWEkJ' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-update-user-v4' '{"country":"ID","dateOfBirth":"ucyQgjqbDRPu","displayName":"EnergeticCubicAxolotlFC2FAF","languageTag":"itIhUQePWOBZ","userName":"AmbidextrousDistortedAardvark7BFADF"}' 'DnyIHRRFQGxE' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-update-user-email-address-v4' '{"code":"EWgPycNZkrdQ","emailAddress":"CONFINEDELDERBERRY+EF7881@fakemail.com"}' 'XvuMideubhEu' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-list-user-roles-v4' 'nRiMapIKeuWk' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-update-user-role-v4' '{"assignedNamespaces":["mzZqHMReAwTp"],"roleId":"b2ba6ddb9d1e4dd9ad5be0de4a6b7bca"}' 'RPgkiFZUvJBh' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-add-user-role-v4' '{"assignedNamespaces":["rFxVkXenyQGP"],"roleId":"ac59db644cc75ffca9adccec04408d63"}' 'tbVbLJgwWIbd' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-remove-user-role-v4' '{"assignedNamespaces":["PcEkcZTkGjkd"],"roleId":"1935216acf53d97a155c60a1ef248eb1"}' 'WHJcjJJxoqmk' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-roles-v4' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-create-role-v4' '{"adminRole":true,"isWildcard":false,"roleName":"BShgvvzTORAL"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-get-role-v4' 'WpvYJkLwOMtE' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-delete-role-v4' 'vsemNJRzrMDc' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-update-role-v4' '{"adminRole":true,"isWildcard":true,"roleName":"ShfgBwTTkcvW"}' 'ROSHdDwrEYPv' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-update-role-permissions-v4' '{"permissions":[{"action":998,"resource":"vNZWohvzqBZi","schedAction":696,"schedCron":"aeBKCOznERtv","schedRange":["KdlQKPkBreIb"]}]}' 'MQBukqviWNzS' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-add-role-permissions-v4' '{"permissions":[{"action":734,"resource":"AWvkSzjLfrfJ","schedAction":740,"schedCron":"EMoXxqzWqZTX","schedRange":["NrUdkTMumEBI"]}]}' 'JakLlDADhZSD' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-delete-role-permissions-v4' '["iDSSzVyiidbh"]' 'ufnVyFvObtjf' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-list-assigned-users-v4' 'VxnZFrLccveE' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-assign-user-to-role-v4' '{"assignedNamespaces":["RwbgzWTEwghE"],"namespace":"BoisterousCagedDodoEC7E39","userId":"dce1b0c56faaa4f32eea76cbbc2d0adb"}' 'MPGZgXotQYBx' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-revoke-user-from-role-v4' '{"namespace":"ElasticCaloricAxolotlDEC843","userId":"9c6afe775ec3d4e1e5c0b6bd55f6dd7b"}' 'FjLqksQzjrli' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-admin-update-my-user-v4' '{"country":"GB","dateOfBirth":"AoKjHKKQHGNh","displayName":"CagedAmbidextrousCarpCACEF4","languageTag":"ToThrneoEelW","userName":"BamboozledBallisticAxolotl5DEBC7"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-create-user-v4' '{"acceptedPolicies":[{"isAccepted":false,"localizedPolicyVersionId":"MnCxeziaRIqR","policyId":"PsYIJNhMlkYO","policyVersionId":"zNWGaaEvjwde"}],"authType":"LpVgyFoCWvcX","country":"GB","dateOfBirth":"vzsDSbIHoANv","displayName":"EditedElasticAardvarkC54E10","emailAddress":"BIONICANTELOPE+A59085@fakemail.com","password":"*[XYhA(u_?w`(L#>","passwordMD5Sum":"RlTobyIvlDBE","username":"BumptiousCagedEmu0BA6CD"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-create-user-from-invitation-v4' '{"authType":"VZMbmrPUKKti","country":"CN","dateOfBirth":"ugEUXHaepnZL","displayName":"AmphibiousCopiousBeetleEF1B01","password":" expQ3-l9z@O<oCe","username":"EccentricBionicBeetle7BAC4E"}' 'cjQCsciXhIqc' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-update-user-v4' '{"country":"GB","dateOfBirth":"GzuXerwrGnpd","displayName":"EnhancedBamboozledChipmunk0FF3EF","languageTag":"DVRUCxKGbcoC","userName":"BrokenAutonomousBadgerCA46CD"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-update-user-email-address-v4' '{"code":"VmZrOmolDcnf","emailAddress":"ENRAGEDDATE+FCEE73@fakemail.com"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-upgrade-headless-account-with-verification-code-v4' '{"code":"yheWWzjVbuiX","country":"IE","dateOfBirth":"BqqSqvOXOTor","displayName":"AgedCaloricEagle74270F","emailAddress":"CALORICCANTALOUPE+D0ADDA@fakemail.com","password":"Vh6hDH63>F)f!2B4","username":"DefeatedEnergeticChipmunk5BECE4"}' '--login_as' 'client'
'python3' '-m' 'accelbyte_py_sdk' 'iam-public-upgrade-headless-account-v4' '{"emailAddress":"CARNIVOROUSFUDGE+06AAF0@fakemail.com","password":"c<4}hs(KC=$J=QXb","username":"EnhancedDemocraticAntelope3CAEB9"}' '--login_as' 'client'