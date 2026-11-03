from typing import Final

class UrlRouteName:
    # Constant and static Properties statiques FOR SESSION AND ACCOUNT
    ERROR_PAGE: Final[str] = "error-page/"
    ERROR_NAME: Final[str] = "error-page"

    ADMIN_PAGE: Final[str] = "admin/"
    ADMIN_NAME: Final[str] = "admin"

    COMPANY_ENTRY_PAGE: Final[str] = "company-entry/"
    COMPANY_ENTRY_NAME: Final[str] = "company-entry"

    LOGIN_PAGE: Final[str] = "login/"
    LOGIN_NAME: Final[str] = "login"

    PASSWORD_RESET_PAGE: Final[str] = "password-reset/"
    PASSWORD_RESET_NAME: Final[str] = "password-reset"

    CREATE_ACCOUNT_PAGE: Final[str] = "create-account/"
    CREATE_ACCOUNT_NAME: Final[str] = "create-account"


    # Constant and static Properties statiques FOR COMPANY
    COMPANIES_LIST_PAGE: Final[str] = "companies/"
    COMPANIES_LIST_NAME: Final[str] = "companies"
    
    COMPANY_CREATE_PAGE: Final[str] = "companies/create/"
    COMPANY_CREATE_NAME: Final[str] = "company-create"

    COMPANY_UPDATE_PAGE: Final[str] = "companies/<int:company_id>/edit/"
    COMPANY_UPDATE_NAME: Final[str] = "company-update"

    COMPANY_MANAGE_BD_PAGE: Final[str] = "companies/<int:company_id>/manage/"
    COMPANY_MANAGE_BD_NAME: Final[str] = "company-manage"

    COMPANY_DELETE_PAGE: Final[str] = "companies/<int:company_id>/delete/"
    COMPANY_DELETE_NAME: Final[str] = "company-delete"

    # Constant and static Properties statiques FOR SCHOOL
    SCHOOLS_LIST_PAGE: Final[str] = "schools/"
    SCHOOLS_LIST_NAME: Final[str] = "schools"
        
    SCHOOL_CREATE_PAGE: Final[str] = "schools/create/"
    SCHOOL_CREATE_NAME: Final[str] = "school-create"
    
    SCHOOL_UPDATE_PAGE: Final[str] = "schools/<int:school_id>/edit/"
    SCHOOL_UPDATE_NAME: Final[str] = "school-update"
    
    #SCHOOL_MANAGE_BD_PAGE: Final[str] = "schools/<int:school_id>/manage/"
    #SCHOOL_MANAGE_BD_NAME: Final[str] = "school-manage"
    
    SCHOOL_DELETE_PAGE: Final[str] = "schools/<int:school_id>/delete/"
    SCHOOL_DELETE_NAME: Final[str] = "school-delete"

