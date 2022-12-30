import pandas as pd
import logging


LOG = logging.getLogger("Builder")
FILE_NAME = "Application Assessment"
SRC_PATH = "src"
DEST_PATH = "dest"


logging.basicConfig(level=logging.INFO)


def main():
    # Loads
    LOG.info("Loads data")
    data = (
        pd.read_table(
            f"{SRC_PATH}/{FILE_NAME}.md",
            sep="|",
            header=0,
            skipinitialspace=True,
            encoding="utf-8",
        )
        .dropna(axis=1, how="all")
        .iloc[1:]
    )

    # Sanitize
    LOG.info("Sanitize data")
    data.rename(columns=lambda x: x.strip(), inplace=True)
    data = data.transform(lambda x: x.str.strip() if x.dtype == "object" else x)

    # Transform before outputs
    LOG.info("Transform")
    data.fillna("", inplace=True)

    # Beautifier
    LOG.info("Beautifier")
    data.sort_values(by=data.columns.tolist(), inplace=True)

    # Outputs
    LOG.info("Output to Excel")
    data.to_excel(
        f"{DEST_PATH}/{FILE_NAME}.xlsx", sheet_name="Application #1", index=False
    )

    LOG.info("Output to CSV")
    data.to_csv(f"{DEST_PATH}/{FILE_NAME}.csv", index=False)

    LOG.info("Output to Markdown")
    data.to_markdown(f"{DEST_PATH}/{FILE_NAME}.md", index=False)


main()
