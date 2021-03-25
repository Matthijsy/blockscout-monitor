# Blockscout monitor
This project uses the [blockscout GraphQL API](https://blockscout.com/etc/mainnet/graphiql) to follow certain addresses. It can notify you when there has been interaction with a certain address. 

### Setup
In order to setup there are 2 steps needed. The first one is to setup an IFTT integration that can notify you.
Go to [iftt](https://ifttt.com), setup a new applet with as first step an incoming webhook. The second step should be the way to notify yourself (for example email). If you want to include the address and the amount of transactions this will be set in `Value1` and `Value2` of IFTT.

The second step is to setup your addresses in main.py line9. The key should be the address, the value the amount of transactions it can have before alerting. Then you can regularly run this script using `WEBHOOK_URL=<IFTT webhook url> python3 blockscout_monitor/main.py`.
