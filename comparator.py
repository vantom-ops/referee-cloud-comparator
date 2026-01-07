from rules import (
    ec2_rules,
    lambda_rules,
    rds_rules,
    ecs_rules,
    firebase_rules
)


def compare_services(traffic, budget, ops):
    return {
        "AWS EC2": ec2_rules(traffic, budget, ops),
        "AWS Lambda": lambda_rules(traffic, budget, ops),
        "AWS RDS": rds_rules(traffic, budget, ops),
        "AWS ECS": ecs_rules(traffic, budget, ops),
        "Firebase": firebase_rules(traffic, budget, ops)
    }
