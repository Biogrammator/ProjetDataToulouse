# API: DATASET de DATA Toulouse

 Important à savoir :

## Limites des requêtes

integer [ -1 .. 100 ]

Default: 10

Number of items to return.

To use with the `offset` parameter to implement pagination.

The maximum possible value depends on whether the query contains a `group_by` clause or not.

For a query **without** a `group_by`:

- the maximum value for `limit` is 100,
- `offset+limit` should be less than 10000

For a query **with** a `group_by`:

- the maximum value for `limit` is 20000,
- `offset+limit` should be less than 20000

> Donc en règle générale on est limité sur les demandes possibles. De ce fait si les jeux de données sont trop grands, on doit nécessairement filtrer avec l'api.

- While the `records` endpoint is subject to a [limited number of returned records](https://help.huwise.com/apis/ods-explore-v2/#tag/Dataset/operation/getRecords), the `exports` endpoint has no limitations.
