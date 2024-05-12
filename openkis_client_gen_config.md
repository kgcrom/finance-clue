# Autorest config

```yaml
title: OpenKISClient
namespace: openkis
python: true
black: true
input-file: OpenKis-oas.yaml
output-folder: stock_clue
verbose: true
version-tolerant: true
override-client-name: GenOpenKisClient
package-version: 0.0.1

add-credential: true
credential-default-policy-type: BearerTokenCredentialPolicy
credential-scopes: https://openapi.koreainvestment.com:9443

directive:
  - from: openapi-document
    where: '$.components.parameters[*]'
    transform: >
      $["x-ms-parameter-location"] = "method";

  # Floating IP operations have been deprecated in favor of reserved IPs.
  - remove-operation: floatingIPs_get
  - remove-operation: floatingIPs_create
  - remove-operation: floatingIPs_list
  - remove-operation: floatingIPs_delete
  - remove-operation: floatingIPsAction_get
  - remove-operation: floatingIPsAction_list
  - remove-operation: floatingIPsAction_post

  - from: openapi-document
    where: '$.components.responses.unauthorized'
    transform: >
      $["x-ms-error-response"] = true;
  - from: openapi-document
    where: '$..["log_line_prefix"]'
    transform: >
      $["x-ms-enum"] = {
        "name": "PostfixLogLinePrefix",
        "modelAsString": false,
        "values": [
          {
            "value": "pid=%p,user=%u,db=%d,app=%a,client=%h",
            "name": "First Option"
          },
          {
            "value": "%m [%p] %q[user=%u,db=%d,app=%a]",
            "name": "Second Option"
          },
          {
            "value": "%t [%p]: [%l-1] user=%u,db=%d,app=%a,client=%h",
            "name": "Third Option"
          }
        ]
      };
```
