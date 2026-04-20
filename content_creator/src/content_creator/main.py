#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from content_creator.crew import ContentCreator

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    product_website = input("Enter the product website URL: \n")
    product_details = input("Any extra details about the product and or the content you're creating: \n")
    inputs = {
        'topic': product_details,
        'product_website': product_website,
        'product_details': product_details,
        'current_year': str(datetime.now().year)
    }

    result = ContentCreator().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n==== FINAL DECISION ====\n\n")
    print(result.raw)

    try:
        ContentCreator().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
 
    run()

