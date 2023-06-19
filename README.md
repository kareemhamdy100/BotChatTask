# BotChatTask

This is a small mock REST API for creating a chat app that accepts questions and provides answers within the app.

## Model Description

The model is designed to follow these steps:

1. The client-side initiates a question.
2. The client-side can block the user from asking new questions and start a timer.
3. After the timer finishes, the client-side retrieves the message by ID and checks if it has an answer. If it does, it shows the answer to the user. If not, it repeats step 2.
4. The client-side can provide feedback on the message by giving it a thumbs-up or thumbs-down. The message should always contain an answer.
5. JWT authentication is used for all these interactions.

This approach aims to solve the problem of delayed responses when asking for an answer. By implementing this flow, users can receive answers more efficiently.

## Possible Improvements

To improve the project, consider the following steps:

1. Implement a well-structured file organization for the project.
2. Use a `.env` file to store settings and secrets, enhancing security and configurability.
3. Enhance the authentication model to include a way to refresh tokens for better security.
4. Add a signup module to allow users to create new accounts.
5. Write comprehensive tests to ensure the code's correctness and reliability.
6. Implement pagination for lists to handle large datasets more effectively.
7. Modify the message model to prevent long-answer messages from being returned entirely from the server. Consider implementing a solution to split and retrieve long messages.
8. Strengthen the validation mechanisms for all inputs and endpoints.
9. Handle client-side delays by allowing clients to receive answers after the timer finishes. Implement server-side notifications using FCM (Firebase Cloud Messaging) and provide the message ID for the client to fetch in real-time.
10. Develop a module to integrate with third-party models or providers, making it easier to add new models or providers. This could be made configurable through settings or dynamically determined based on the user type derived from JWT.

By addressing these improvements, the project will have a more robust and scalable architecture, better security measures, and enhanced user experience.
