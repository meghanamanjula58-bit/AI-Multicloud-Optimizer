
def generate_recommendations(data):

    recommendations = []

    for _, row in data.iterrows():

        if row["CPU"] > 80:

            recommendations.append(
                f"{row['Cloud']}: High CPU usage. "
                "Review workload and resource allocation."
            )

        if row["Memory"] > 80:

            recommendations.append(
                f"{row['Cloud']}: High memory usage. "
                "Review memory requirements."
            )

        if row["Storage"] > 85:

            recommendations.append(
                f"{row['Cloud']}: High storage usage. "
                "Review storage consumption."
            )

        if row["CPU"] < 20:

            recommendations.append(
                f"{row['Cloud']}: Low CPU usage. "
                "Review whether resources are oversized."
            )

    if not recommendations:

        recommendations.append(
            "All cloud resources are within the selected thresholds."
        )

    return recommendations
