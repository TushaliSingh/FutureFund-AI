from io import BytesIO
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
    Image,
)

from utils.chart_generator import (
    create_sip_growth_chart,
    create_portfolio_chart,
    create_wealth_projection_chart,
)


class FinancialReportGenerator:
    """
    Generates a professional financial report.
    """

    def __init__(self):
        self.buffer = BytesIO()

    def _add_header_footer(self, canvas, doc):
        """
        Adds a professional header and footer
        to every page of the report.
        """

        canvas.saveState()

        # ---------------- Header ----------------

        canvas.setFont("Helvetica-Bold", 12)

        canvas.drawString(
            inch,
            10.5 * inch,
            "FutureFund AI",
        )

        canvas.setFont("Helvetica", 9)

        canvas.drawRightString(
            7.5 * inch,
            10.5 * inch,
            "Financial Report",
        )

        # ---------------- Footer ----------------

        canvas.setFont("Helvetica", 8)

        canvas.drawString(
            inch,
            0.5 * inch,
            f"Generated: {datetime.now().strftime('%d %b %Y')}",
        )

        canvas.drawRightString(
            7.5 * inch,
            0.5 * inch,
            f"Page {canvas.getPageNumber()}",
        )

        canvas.restoreState()

    def generate_report(self, report_data: dict):

        doc = SimpleDocTemplate(self.buffer)

        styles = getSampleStyleSheet()

        title_style = styles["Heading1"]
        title_style.alignment = TA_CENTER
        title_style.textColor = colors.darkblue

        story = []

        # ==================================================
        # REPORT HEADER
        # ==================================================

        story.append(
            Paragraph(
                "FutureFund AI",
                title_style,
            )
        )

        story.append(Spacer(1, 8))

        story.append(
            Paragraph(
                "AI-Powered Investment & Financial Planning Platform",
                styles["Heading3"],
            )
        )

        story.append(Spacer(1, 18))

        story.append(
            Paragraph(
                "<b>Financial Report</b>",
                styles["Heading2"],
            )
        )

        story.append(Spacer(1, 15))

        story.append(
            Paragraph(
                f"<b>Prepared For:</b> {report_data.get('username', 'User')}",
                styles["BodyText"],
            )
        )

        story.append(
            Paragraph(
                f"<b>Generated On:</b> {datetime.now().strftime('%d %B %Y')}",
                styles["BodyText"],
            )
        )

        story.append(Spacer(1, 25))

        # ==================================================
        # INTRODUCTION
        # ==================================================

        story.append(
            Paragraph(
                (
                    "This report summarizes your financial profile using "
                    "FutureFund AI. It includes key financial metrics, "
                    "AI-powered investment insights, portfolio allocation, "
                    "and future wealth projections."
                ),
                styles["BodyText"],
            )
        )

        story.append(Spacer(1, 25))

        # ==================================================
        # FINANCIAL SUMMARY
        # ==================================================

        story.append(
            Paragraph(
                "<b>Financial Summary</b>",
                styles["Heading2"],
            )
        )

        story.append(Spacer(1, 10))

        table_data = [
            ["Metric", "Value"],
            [
                "Estimated Portfolio Value",
                f"₹{report_data.get('estimated_net_worth', 0):,.0f}",
            ],
            [
                "Monthly Savings",
                f"₹{report_data.get('monthly_savings', 0):,.0f}",
            ],
            [
                "Financial Health Score",
                f"{report_data.get('financial_score', 0)}/100",
            ],
            [
                "Recommended SIP",
                f"₹{report_data.get('recommended_sip', 0):,.0f}",
            ],
        ]

        summary_table = Table(
            table_data,
            colWidths=[250, 180],
        )

        summary_table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                    ("GRID", (0, 0), (-1, -1), 1, colors.grey),
                    ("BOX", (0, 0), (-1, -1), 1.2, colors.black),
                    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                ]
            )
        )

        story.append(summary_table)

        story.append(Spacer(1, 25))

        # ==================================================
        # AI RECOMMENDATION
        # ==================================================

        story.append(
            Paragraph(
                "<b>AI Recommendation Summary</b>",
                styles["Heading2"],
            )
        )

        story.append(Spacer(1, 10))

        recommendation = report_data.get("recommendation")

        if recommendation:

            story.append(
                Paragraph(
                    f"<b>Suggested Monthly SIP:</b> ₹{recommendation['sip']:,}",
                    styles["BodyText"],
                )
            )

            story.append(Spacer(1, 8))

            story.append(
                Paragraph(
                    "<b>Recommended Portfolio Allocation</b>",
                    styles["BodyText"],
                )
            )

            for asset, allocation in recommendation["portfolio"].items():

                story.append(
                    Paragraph(
                        f"• {asset}: {allocation}%",
                        styles["BodyText"],
                    )
                )

            story.append(Spacer(1, 8))

            story.append(
                Paragraph(
                    "<b>Investment Strategy</b>",
                    styles["BodyText"],
                )
            )

            for strategy in recommendation["strategy"]:

                story.append(
                    Paragraph(
                        f"• {strategy}",
                        styles["BodyText"],
                    )
                )

            story.append(Spacer(1, 8))

            story.append(
                Paragraph(
                    "<b>Improvement Suggestions</b>",
                    styles["BodyText"],
                )
            )

            if recommendation["improvements"]:

                for item in recommendation["improvements"]:

                    story.append(
                        Paragraph(
                            f"• {item}",
                            styles["BodyText"],
                        )
                    )

            else:

                story.append(
                    Paragraph(
                        "Excellent financial profile. No improvements suggested.",
                        styles["BodyText"],
                    )
                )

        else:

            story.append(
                Paragraph(
                    "No AI recommendation has been generated yet.",
                    styles["BodyText"],
                )
            )

        story.append(Spacer(1, 25))
                # ==================================================
        # SIP GROWTH CHART
        # ==================================================

        story.append(
            Paragraph(
                "<b>SIP Growth Projection</b>",
                styles["Heading2"],
            )
        )

        story.append(Spacer(1, 12))

        story.append(
            Image(
                create_sip_growth_chart(),
                width=430,
                height=250,
            )
        )

        story.append(Spacer(1, 25))

        # ==================================================
        # PORTFOLIO ALLOCATION CHART
        # ==================================================

        story.append(
            Paragraph(
                "<b>Portfolio Allocation</b>",
                styles["Heading2"],
            )
        )

        story.append(Spacer(1, 12))

        story.append(
            Image(
                create_portfolio_chart(),
                width=320,
                height=320,
            )
        )

        story.append(Spacer(1, 25))

        # ==================================================
        # WEALTH PROJECTION CHART
        # ==================================================

        story.append(
            Paragraph(
                "<b>Wealth Projection</b>",
                styles["Heading2"],
            )
        )

        story.append(Spacer(1, 12))

        story.append(
            Image(
                create_wealth_projection_chart(),
                width=430,
                height=250,
            )
        )

        story.append(Spacer(1, 25))

        # ==================================================
        # DISCLAIMER
        # ==================================================

        story.append(
            Paragraph(
                "<b>Disclaimer</b>",
                styles["Heading2"],
            )
        )

        story.append(Spacer(1, 8))

        story.append(
            Paragraph(
                (
                    "This report has been automatically generated by "
                    "<b>FutureFund AI</b> for educational purposes. "
                    "The investment suggestions, financial projections, "
                    "portfolio allocations, and analytics presented in this "
                    "report should not be considered professional financial "
                    "or investment advice. Always consult a qualified "
                    "financial advisor before making investment decisions."
                ),
                styles["BodyText"],
            )
        )

        story.append(Spacer(1, 20))

        # ==================================================
        # REPORT FOOTER
        # ==================================================

        story.append(
            Paragraph(
                "<font size='9' color='grey'>"
                "© FutureFund AI • AI-Powered Investment & Financial Planning Platform"
                "</font>",
                styles["BodyText"],
            )
        )

        # ==================================================
        # BUILD PDF
        # ==================================================

        doc.build(
            story,
            onFirstPage=self._add_header_footer,
            onLaterPages=self._add_header_footer,
        )

        pdf = self.buffer.getvalue()

        self.buffer.close()

        return pdf