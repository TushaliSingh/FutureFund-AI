import pandas as pd
from io import BytesIO


def history_to_csv(history):

    df = pd.DataFrame(
        history,
        columns=[
            "Feature",
            "Result",
            "Created At"
        ]
    )

    return df.to_csv(index=False).encode("utf-8")


def history_to_excel(history):

    df = pd.DataFrame(
        history,
        columns=[
            "Feature",
            "Result",
            "Created At"
        ]
    )

    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name="Investment History"
        )

    output.seek(0)

    return output.getvalue()