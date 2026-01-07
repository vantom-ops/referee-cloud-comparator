def ec2_rules(traffic, budget, ops):
    pros = []
    cons = []
    score = 0

    if traffic == "High":
        pros.append("Best for sustained workloads")
        score += 3
    else:
        cons.append("Not ideal for unpredictable traffic")

    if ops == "High":
        pros.append("Full infrastructure control")
        score += 2
    else:
        cons.append("Requires DevOps effort")

    return {
        "pros": pros,
        "cons": cons,
        "score": score
    }


def lambda_rules(traffic, budget, ops):
    pros = []
    cons = []
    score = 0

    if traffic == "Spiky":
        pros.append("Auto-scales instantly")
        score += 3
    else:
        cons.append("Cold start overhead")

    if ops == "Low":
        pros.append("No server management")
        score += 3

    return {
        "pros": pros,
        "cons": cons,
        "score": score
    }


def rds_rules(traffic, budget, ops):
    pros = []
    cons = []
    score = 2

    pros.append("Managed relational database")

    if ops == "Low":
        pros.append("Automated backups and patching")

    return {
        "pros": pros,
        "cons": cons,
        "score": score
    }


def ecs_rules(traffic, budget, ops):
    pros = []
    cons = []
    score = 0

    if ops == "High":
        pros.append("Powerful container orchestration")
        score += 3
    else:
        cons.append("Steep learning curve")

    return {
        "pros": pros,
        "cons": cons,
        "score": score
    }


def firebase_rules(traffic, budget, ops):
    pros = []
    cons = []
    score = 0

    if ops == "Low":
        pros.append("Very fast setup")
        score += 3

    cons.append("Vendor lock-in")

    return {
        "pros": pros,
        "cons": cons,
        "score": score
    }
