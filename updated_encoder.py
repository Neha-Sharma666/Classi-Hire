from sklearn.preprocessing import LabelEncoder
import pickle
import os


categories = [
    'Data Science', 'HR', 'Advocate', 'Arts', 'Web Designing',
    'Mechanical Engineer', 'Sales', 'Health and fitness',
    'Civil Engineer', 'Java Developer', 'Business Analyst',
    'SAP Developer', 'Automation Testing', 'Electrical Engineering',
    'Operations Manager', 'Python Developer', 'DevOps Engineer',
    'Network Security Engineer', 'PMO', 'Database', 'Hadoop',
    'ETL Developer', 'DotNet Developer', 'Blockchain', 'Testing'
]


le = LabelEncoder()
le.fit(categories)


os.makedirs('model', exist_ok=True)

# Save the updated encoder
with open('model/encoder.pkl', 'wb') as f:
    pickle.dump(le, f)

print("Updated LabelEncoder saved!")
print("Categories in LabelEncoder:", le.classes_)
