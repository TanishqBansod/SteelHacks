import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPEN_API_KEY')


def summarize_reviews(reviews_chunk):
    response = openai.ChatCompletion.create(
        model="gpt-4",  # You can use gpt-3.5-turbo for cost-efficiency
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes people reviews."},
            # {"role": "user", "content": f"Please summarize these product reviews: {reviews_chunk}"},
            {"role": "user",
             "content": f"Here are few reviews of a person, summarize it and tell where the person is good and where the person is not very good in one line few words: {reviews_chunk}"}
        ],
        max_tokens=300,  # Adjust based on the length of the summary
        temperature=0.5  # Adjust for more creative vs. focused summaries
    )
    return response['choices'][0]['message']['content']


class ReviewModel:
    def __init__(self, user_id: str, batch_size: int):
        self.user_id = user_id
        self.batch_size = batch_size
        self.user_reviews = [
            "Review 1: He is a good manager, he helped me in becoming a good programmer",
            "Review 2: Good manager",
            "Review 3: Not so good manager, zero personality, doesn't even know how to talk to interns",
            "Review 4: He is a good manager, he helped me in becoming a good programmer",
            "Review 5: Good manager",
            "Review 6: Not so good manager, zero personality, doesn't even know how to talk to interns",
            "Review 7: He is a good manager, he helped me in becoming a good programmer",
            "Review 8: Good manager",
            "Review 9: Not so good manager, zero personality, doesn't even know how to talk to interns"
            # Add all your reviews here
        ]

    def get_all_reviews(self):
        # this function should fetch all the reviews of a user from DB
        return []

    def final_review(self):
        if not self.user_reviews:
            self.user_reviews = self.get_all_reviews()

        summaries = []

        for i in range(0, len(self.user_reviews), self.batch_size):
            reviews_chunk = " ".join(self.user_reviews[i:i + self.batch_size])
            summary = summarize_reviews(reviews_chunk)
            summaries.append(summary)
        final_summary = summarize_reviews(" ".join(summaries))

        print("Final Product Review Ready:")
        return final_summary


if __name__ == '__main__':
    cl = ReviewModel("sdf", 24)
    print(cl.final_review())
