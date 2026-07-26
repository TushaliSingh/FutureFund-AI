from io import BytesIO

import matplotlib.pyplot as plt


def _save_chart(fig):
    """
    Saves a matplotlib figure into memory.
    """

    image_buffer = BytesIO()

    plt.savefig(
        image_buffer,
        format="png",
        dpi=200,
        bbox_inches="tight"
    )

    plt.close(fig)

    image_buffer.seek(0)

    return image_buffer


def create_sip_growth_chart():

    years = [1, 2, 3, 4, 5]

    investment = [120000, 240000, 360000, 480000, 600000]

    portfolio = [126000, 270000, 432000, 620000, 850000]

    fig, ax = plt.subplots(figsize=(7, 4))

    ax.plot(
        years,
        investment,
        marker="o",
        linewidth=2,
        label="Investment"
    )

    ax.plot(
        years,
        portfolio,
        marker="o",
        linewidth=2,
        label="Portfolio Value"
    )

    ax.set_title("SIP Growth Projection")
    ax.set_xlabel("Years")
    ax.set_ylabel("Amount (₹)")
    ax.legend()
    ax.grid(True)

    return _save_chart(fig)


def create_portfolio_chart():

    labels = [
        "Equity",
        "Debt",
        "Gold",
        "Cash"
    ]

    values = [
        60,
        25,
        10,
        5
    ]

    fig, ax = plt.subplots(figsize=(5, 5))

    ax.pie(
        values,
        labels=labels,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title("Portfolio Allocation")

    return _save_chart(fig)


def create_wealth_projection_chart():

    years = [
        2026,
        2027,
        2028,
        2029,
        2030
    ]

    wealth = [
        300000,
        450000,
        620000,
        820000,
        1050000
    ]

    fig, ax = plt.subplots(figsize=(7, 4))

    ax.bar(
        years,
        wealth
    )

    ax.set_title("Projected Wealth")

    ax.set_xlabel("Year")

    ax.set_ylabel("₹")

    return _save_chart(fig)