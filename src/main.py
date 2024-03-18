from fastapi import FastAPI
from src.users.routers import router as user_router
from src.accounts.routers import router as account_router
from src.transactions.routers import router as transaction_router
from src.categories.routers import router as category_router
from src.budgets.routers import router as budget_router
from src.expenses.routers import router as expense_router


app = FastAPI()

app.include_router(user_router)

app.include_router(account_router)

app.include_router(transaction_router)

app.include_router(category_router)

app.include_router(budget_router)

app.include_router(expense_router)


