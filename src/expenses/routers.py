
from src.utils.container import get_container
from src.utils.dependencies import GetListDependency, RetrieveDependency, DeleteDependency
from src.expenses.repository import ExpenseRepo
from src.expenses.dependencies import ExpenseCreateDependency
from fastapi import APIRouter

router = APIRouter(prefix="/expense", tags=["Expenses"])

router.add_api_route("/get_expenses", get_container(ExpenseRepo).resolve(GetListDependency), methods=["GET"])

router.add_api_route("/get_expense", get_container(ExpenseRepo).resolve(RetrieveDependency), methods=["GET"])

router.add_api_route("/create_expense", get_container(ExpenseRepo).resolve(ExpenseCreateDependency), methods=["POST"])

router.add_api_route("/delete_expense", get_container(ExpenseRepo).resolve(DeleteDependency), methods=["DELETE"])
