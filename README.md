# datacrunch-backtest

A small backtesting utility.

[![PyTest](https://github.com/datacrunch-com/datacrunch-backtest/actions/workflows/pytest.yml/badge.svg)](https://github.com/datacrunch-com/datacrunch-backtest/actions/workflows/pytest.yml)

- [datacrunch-backtest](#datacrunch-backtest)
  - [Usage](#usage)
    - [Options](#options)
      - [Exporters](#exporters)
        - [Console](#console)
        - [Influx](#influx)
        - [QuantStats](#quantstats)
      - [Data Sources](#data-sources)
        - [Yahoo](#yahoo)
        - [CoinMarketCap](#coinmarketcap)
        - [File](#file)
          - [.parquet](#parquet)

## Usage

```bash
python3 main.py [OPTIONS]
```

### Options

| Option | Value | Default | Format | Description |
| --- | --- | --- | --- | --- |
| `--start` | `<start date>` | `today - 1 year` | `date` (ISO-8601) | The starting date of the backtesting. If the value is before the first ordering day, the value will be discarded. |
| `--end` | `<end date>` | `today` | `date` (ISO-8601) | The ending date of the backtesting. If the value is after today, the value will be discarded. |
| `--order-file` | `<file>` | | `path` | The single order file to use. The file must contain symbol, quantity and date information. |
| `--single-file-provider-column-date` | `<column>` | `date` | `string` | Change the date column name to use. |
| `--single-file-provider-column-symbol` | `<column>` | `symbol` | `string` | Change the symbol column name to use. |
| `--single-file-provider-column-quantity` | `<column>` | `quantity` | `string` | Change the quantity column name to use. |
| `--order-files` | `<directory>` | | `path` | The directory of order file to use. The filename must be a date. The file must contain symbol and quantity information. |
| `--order-files-extension` | `<extension>` | `csv`  | `[csv, json]` | Change the file extension to use when listing for order files. |
| `--initial-cash` | `<amount>` | `100_000` | `number` | Change the initial cash to use for the backtesting. |
| `--quantity-mode` | `<mode>` | `percent` | `[percent, share]` | If the mode is `share`, all quantities will be interpreted as integers. If the mode is `percent`, all values will be multiplied by the current cash value. |
| `--auto-close-others` | | `false` | | Should other position be closed after an ordering? |
| `--weekends` | | `false` | | Enable ordering on weekends. |
| `--holidays` | | `false` | | Enable ordering on holidays. |
| `--symbol-mapping` | `<mapping>` | | `path` (.json) | Specify a custom symbol mapping file enabling vendor-id translation. |
| `--no-caching` | | `false` | | Disable prices caching. |
| `--fee-model` | `<model>` | | `expression` or `constant` | Specify a fee model to use. The value can be a `constant`. Or an expression that allow the usage of the `price` and `quantity` variable. <br /> Example: `abs(price * quantity) * 0.1` |

#### Exporters

Multiple exporters can be enabled at one time.

##### Console

The console exporter allows a quick look at the backtest.

| Option | Value | Default | Format | Description |
| --- | --- | --- | --- | --- |
| `--console` | | `false` | | Enable the console exporter. |
| `--console-format` | `<format>` | `text` | `[text, json]` | Change the output format. |
| `--console-file` | `<file>` | `out` | `[out, err]` | Change the output file. |
| `--console-hide-skips` | | `false` | | Do not the skipped days. |
| `--console-text-no-color` | | `false` | | Disable colors in the output. (only if the format is `text`) |

##### Influx

Export the generated data to an Influx database. <br />
Making it easier to plot the values using software like Grafana.

| Option | Value | Default | Format | Description |
| --- | --- | --- | --- | --- |
| `--influx` | | `false` | | Enable the influx exporter. |
| `--influx-host` | `<host>` | `localhost` | `string` | Specify the remote influx address. |
| `--influx-port` | `<port>` | `8086` | `number` | Specify the remote influx port. |
| `--influx-database` | `<database>` | `backtest` | `string` | Specify the influx database to use. |
| `--influx-measurement` | `<measurement>` | `snapshots` |`string` | Specify the table name to use. |
| `--influx-key` | `<key>` | `test` | `string` | Specify the unique key to use. **Previous data with the same key will be deleted!** |

##### QuantStats

Generate a tearsheet from the backtest data.

| Option | Value | Default | Format | Description |
| --- | --- | --- | --- | --- |
| `--quantstats` | | `false` | | Enable the quantstats exporter. |
| `--quantstats-output-file-html` | `<file>` | `report.html` | `path` | Specify the output file containing the tearsheet. |
| `--quantstats-output-file-csv` | `<file>` | `report.csv` | `path` | Specify the output file containing raw returns. |
| `--quantstats-benchmark-ticker` | `<ticker>` | `SPY` | `symbol` | Specify the ticker to use as a benchmark in the tearsheet. |
| `--quantstats-auto-delete` | | `false` | | Automatically delete the previous report files if they are present. |

#### Data Sources

Only one data source can be used at once.

##### Yahoo

| Option | Value | Default | Format | Description |
| --- | --- | --- | --- | --- |
| `--yahoo` | | `false` | | Enable yahoo as the data source. |

##### CoinMarketCap

| Option | Value | Default | Format | Description |
| --- | --- | --- | --- | --- |
| `--coinmarketcap` | | `false` | | Enable coinmarketcap as the data source. |
| `--coinmarketcap-force-mapping-refresh` | | `false` | | Force a mapping refresh. This is usually only done automatically the first time of using this data source. |
| `--coinmarketcap-page-size` | `<size>` | `10_000` | `number` | Specify the page size while building the mapping. |

##### File

Use a static file as a price data source.

###### .parquet

| Option | Value | Default | Format | Description |
| --- | --- | --- | --- | --- |
| `--file-parquet` | `<file>` | | `path` | Use a static `.parquet` file as a the data source. |
| `--file-parquet-column-date` | `<column>` | `date` | `string` | Specify the name of column containing the dates informations. |
| `--file-parquet-column-symbol` | `<column>` | `symbol` | `string` | Specify the name of column containing the symbols informations. |
| `--file-parquet-column-price` | `<column>` | `price` | `string` | Specify the name of column containing the prices informations. |
