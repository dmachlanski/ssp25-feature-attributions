load('data/pbc2.rda')
write.csv(pbc2, 'data/pbc2.csv', row.names=FALSE)

load('data/pbc2.id.rda')
write.csv(pbc2.id, 'data/pbc2_id.csv', row.names=FALSE)

load('data/aids.rda')
write.csv(aids, 'data/aids.csv', row.names=FALSE)

load('data/aids.id.rda')
write.csv(aids.id, 'data/aids_id.csv', row.names=FALSE)

load('data/prothro.rda')
write.csv(prothro, 'data/prothro.csv', row.names=FALSE)

load('data/prothros.rda')
write.csv(prothros, 'data/prothros.csv', row.names=FALSE)