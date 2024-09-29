document.addEventListener('DOMContentLoaded', () => {
    // Handle Create Account Form Submission
    const createAccountForm = document.getElementById('createAccountForm');
    if (createAccountForm) {
        createAccountForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const name = document.getElementById('name').value;
            const position = document.getElementById('position').value;

            // Send POST request to /user endpoint
            const response = await fetch('/user', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ name, position }) // Send name and position
            });

            const result = await response.json();

            // Display the result in the form
            document.getElementById('result').textContent = result.user_id
                ? `User created successfully! Your User ID: ${result.user_id}`
                : 'Error creating user.';
        });
    }

    // Handle Submit Review Form Submission
    const submitReviewForm = document.getElementById('submitReviewForm');
    if (submitReviewForm) {
        submitReviewForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const fromId = document.getElementById('fromId').value;
            const toId = document.getElementById('toId').value;
            const review = document.getElementById('review').value;

            // Send POST request to /submit_review endpoint
            const response = await fetch('/submit_review', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ from_id: fromId, to_id: toId, review }) // Send fromId, toId, and review
            });

            const result = await response.json();

            // Display success or error message
            document.getElementById('reviewResult').textContent = result.message
                ? `Review submitted successfully!`
                : 'Error submitting review.';
        });
    }

    // Handle Generate Summary Form Submission
    const generateSummaryForm = document.getElementById('generateSummaryForm');
    if (generateSummaryForm) {
        generateSummaryForm.addEventListener('submit', async (e) => {
            e.preventDefault();

            const userId = document.getElementById('userId').value;

            // Send POST request to /generate_final_review endpoint
            const response = await fetch('/generate_final_review', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ user_id: userId }) // Send userId
            });

            const result = await response.json();

            // Display the summary result
            document.getElementById('summaryResult').textContent = result.final_summary
                ? `Summary: ${result.final_summary}`
                : 'Error generating summary.';
        });
    }
});

