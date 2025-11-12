## Reflection

### What worked:
- The Random Forest model turned out to be surprisingly strong for such a small dataset.  
  It didn’t need heavy tuning and still performed really well, which gave me a lot of confidence in how feature selection and data quality matter more than fancy models.  
- The visualizations (Confusion Matrix, ROC, PR curves) made it easier to actually “see” how the model behaves, instead of just relying on accuracy numbers. That part really helped me understand model performance better.

### What didn’t:
- The dataset was quite unbalanced — there are very few Pokémon with Mega Evolutions compared to normal ones.  
  That made me realize how much data imbalance can affect the model, even if accuracy looks high.  
- I also noticed that I ignored some possibly important features like Pokémon Type or Generation. If I revisit this, I’d like to try encoding those to see if it improves prediction logic.
- I initially underestimated the importance of cleaning and organizing the project structure — it took longer, but now I see how it makes everything more maintainable and readable.

### What I learned:
- Building this end-to-end taught me how to connect everything: from cleaning data to training, evaluating, and visualizing results — not just running a model and stopping there.  
- I learned that machine learning isn’t just about getting accuracy — it’s about understanding what the model is doing and how to explain it clearly.  
- Most importantly, I learned how to take feedback from my own mistakes, debug issues, and make the project production-like (with modular code, virtual environment, and documentation).  
- This project reminded me why I enjoy ML — every step taught me something new, and it made me more confident that I can grow fast and learn on the go during the internship.
