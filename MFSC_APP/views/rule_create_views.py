from tkinter import Frame, Label, Entry, Button, ttk


class RuleCreateViews(Frame):
           
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.input_frame = Frame(self)
        self.input_frame.grid(row=0, column=0, padx=5, pady=10,sticky="w")

        self.ref_no_lb = Label(self.input_frame, text="REF NO")
        self.ref_no_lb.grid(row=1, column=0, padx=5, pady=10)
        self.ref_no_input = Entry(self.input_frame)
        self.ref_no_input.grid(row=2, column=0, padx=5, pady=10)

        self.rule_code_lb = Label(self.input_frame, text="RULE_CODE")
        self.rule_code_lb.grid(row=3, column=0, padx=5, pady=10)
        self.rule_code_input = Entry(self.input_frame)
        self.rule_code_input.grid(row=4, column=0, padx=5, pady=10)

        self.rule_des_lb = Label(self.input_frame, text="RULE_DESCRIPTION")
        self.rule_des_lb.grid(row=3, column=1, padx=5, pady=10)
        self.rule_des_input = Entry(self.input_frame)
        self.rule_des_input.grid(row=4, column=1, padx=5, pady=10)

        self.fomula_lb = Label(self.input_frame, text="FORMULA")
        self.fomula_lb.grid(row=3, column=2, padx=5, pady=10)
        self.fomula_input = ttk.Combobox(self.input_frame,
                                         values=[    
                                            "(%)GROUP_OF_ASSETS_MKV/NAV",
                                            "(%)ADVERTISING_EXPENSE/AVG_NAV",
                                            "(%)OTHER_EXPENSE/AVG_NAV",
                                            "(%)CONTRACT_AMT/EXPOSURE(BY_CCY)",
                                            "(%)GLOBAL_EXPOS_LIMIT/NAV(NON_HEDGED)",
                                            "(%)CHANGE_OF_FUND'S_OUTS_UNIT",
                                            "(%)HOLDING_UNIT/OUTS_UNIT(CIS)",
                                            "(%)HOLDING_UNIT/VOTING_RIGHT_SHARE(EQUITY)",
                                            "(%)MKV_OF_ASSETS_BY_ISSUER/NAV",
                                            "(#OF_FLOW)_OF_SAME_AMC_CIS_INV",
                                            "(%)MKV_OF_ASSETS_BY_ISSUER_GROUP/NAV",
                                            "(%)MKV_OF_SAME_AMC_CIS_INVEST/NAV",
                                            "(%)FUND_TYPE_LIMIT(AVERAGE_รอบปี)",
                                            "(%)HOLDING_NOMINAL_AMT_BY_ISSUER/TOTAL_FIN_LIAB",
                                            "(%)HOLDING_NOMINAL_AMT/ISSUE_SIZE",
                                            "(DAYS)PORTFOLIO_MACAULAY_DURATION",
                                            "(UNITS)REMAINING_REGISTERED_UNITS",
                                            "DUP_SELLING_FEE_FOR_SAME_AMC_CIS_INVEST",
                                            "(%)LIMIT_FROM_BENCHMARK_CAL",
                                            "(%)GROUP_OF_ASSETS_MKV/NAV(PRODUCT)",
                                            "(%)FUND_TYPE_LIMIT(AVERAGE_รอบปี)(PRODUCT)"
                                                 ],
                                        state="readonly"
                                        )
        self.fomula_input.grid(row=4, column=2, padx=5, pady=10)
        self.fomula_input.bind("<<ComboboxSelected>>", self.update_condition_combobox)


        '''
        self.OPERATOR1_input = ttk.Combobox(
            self.input_frame,
            values=["=", ">", "<", ">=", "<=", "!="],  # Dropdown options
            state="readonly"  # Prevent user from entering values manually
        )'''


        self.OPEN_PARENTHESIS_lb = Label(self.input_frame, text="OPEN_PARENTHESIS")
        self.OPEN_PARENTHESIS_lb.grid(row=5, column=0, padx=5, pady=10)
        self.OPEN_PARENTHESIS_input = ttk.Combobox(self.input_frame,values=["("
                                        ],
                                        state="normal")
        self.OPEN_PARENTHESIS_input.grid(row=6, column=0, padx=5, pady=10)

        
        self.CONDITION_lb = Label(self.input_frame, text="CONDITION")
        self.CONDITION_lb.grid(row=5, column=1, padx=5, pady=10)
        self.CONDITION_input = ttk.Combobox(self.input_frame,
                                         state="normal"
        )
                                    
        self.CONDITION_input.grid(row=6, column=1, padx=5, pady=10)
        self.CONDITION_input.bind("<<ComboboxSelected>>", self.update_second_combobox)


        self.OPERATOR1_lb = Label(self.input_frame, text="OPERATOR1")
        self.OPERATOR1_lb.grid(row=5, column=2, padx=5, pady=10)
        self.OPERATOR1_input = ttk.Combobox(self.input_frame,values=["=",
                                                                    ">",
                                                                    "<",
                                                                    ">=",
                                                                    "<=",
                                                                    "<>",
                                                                    "IN",
                                                                    "NOT IN"
                                        ],
                                        state="readonly")
        self.OPERATOR1_input.grid(row=6, column=2, padx=5, pady=10)


        self.CONDITION_VALUE_lb = Label(self.input_frame, text="CONDITION_VALUE")
        self.CONDITION_VALUE_lb.grid(row=5, column=3, padx=5, pady=10)
        self.CONDITION_VALUE_input = ttk.Combobox(self.input_frame,state="normal")
        self.CONDITION_VALUE_input.grid(row=6, column=3, padx=5, pady=10)

        self.AND_OR1_lb = Label(self.input_frame, text="AND_OR1")
        self.AND_OR1_lb.grid(row=5, column=4, padx=5, pady=10)
        self.AND_OR1_input = ttk.Combobox(self.input_frame,values=["AND","OR"                
                                        ],
                                        state="readonly")
        self.AND_OR1_input.grid(row=6, column=4, padx=5, pady=10)

        self.CLOSE_PARENTHESIS_lb = Label(self.input_frame, text="CLOSE_PARENTHESIS")
        self.CLOSE_PARENTHESIS_lb.grid(row=5, column=5, padx=5, pady=10)
        self.CLOSE_PARENTHESIS_input = ttk.Combobox(self.input_frame,values=[")"
                                        ],
                                        state="normal")
        self.CLOSE_PARENTHESIS_input.grid(row=6, column=5, padx=5, pady=10)


        self.AND_OR2_lb = Label(self.input_frame, text="AND_OR2")
        self.AND_OR2_lb.grid(row=7, column=0, padx=5, pady=10)
        self.AND_OR2_input = ttk.Combobox(self.input_frame,values=["AND","OR"                
                                        ],
                                        state="readonly")
        self.AND_OR2_input.grid(row=8, column=0, padx=5, pady=10)

        self.OPERATOR2_lb = Label(self.input_frame, text="OPERATOR2")
        self.OPERATOR2_lb.grid(row=7, column=1, padx=5, pady=10)
        self.OPERATOR2_input = ttk.Combobox(self.input_frame,values=["=",
                                                                    ">",
                                                                    "<",
                                                                    ">=",
                                                                    "<="
                                        ],
                                        state="readonly")
        self.OPERATOR2_input.grid(row=8, column=1, padx=5, pady=10)

        self.LIMIT_VALUE_lb = Label(self.input_frame, text="LIMIT_VALUE")
        self.LIMIT_VALUE_lb.grid(row=7, column=2, padx=5, pady=10)
        self.LIMIT_VALUE_input = Entry(self.input_frame)
        self.LIMIT_VALUE_input.grid(row=8, column=2, padx=5, pady=10)

        self.BENCHMARK_CODE_lb = Label(self.input_frame, text="BENCHMARK_CODE")
        self.BENCHMARK_CODE_lb.grid(row=9, column=0, padx=5, pady=10)
        self.BENCHMARK_CODE_input = Entry(self.input_frame)
        self.BENCHMARK_CODE_input.grid(row=10, column=0, padx=5, pady=10)

        self.BENCHMARK_CODE_lb = Label(self.input_frame, text="BENCHMARK_CODE")
        self.BENCHMARK_CODE_lb.grid(row=9, column=0, padx=5, pady=10)
        self.BENCHMARK_CODE_input = Entry(self.input_frame)
        self.BENCHMARK_CODE_input.grid(row=10, column=0, padx=5, pady=10)

        self.PRORATA_lb = Label(self.input_frame, text="PRORATA")
        self.PRORATA_lb.grid(row=9, column=1, padx=5, pady=10)
        self.PRORATA_input = ttk.Combobox(self.input_frame,values=["Y"],state="normal")
        self.PRORATA_input.grid(row=10, column=1, padx=5, pady=10)

        self.CIS_MANAGER_lb = Label(self.input_frame, text="CIS_MANAGER")
        self.CIS_MANAGER_lb.grid(row=9, column=2, padx=5, pady=10)
        self.CIS_MANAGER_input = ttk.Combobox(self.input_frame,values=["Y"],state="normal")
        self.CIS_MANAGER_input.grid(row=10, column=2, padx=5, pady=10)

        self.MKT_DERIVATIVE_lb = Label(self.input_frame, text="MKT_DERIVATIVE")
        self.MKT_DERIVATIVE_lb.grid(row=9, column=3, padx=5, pady=10)
        self.MKT_DERIVATIVE_input = ttk.Combobox(self.input_frame,values=["Y"],state="normal")
        self.MKT_DERIVATIVE_input.grid(row=10, column=3, padx=5, pady=10)

        self.UNDERLYING_CODE_lb = Label(self.input_frame, text="UNDERLYING_CODE")
        self.UNDERLYING_CODE_lb.grid(row=9, column=3, padx=5, pady=10)
        self.UNDERLYING_CODE_input = Entry(self.input_frame)
        self.UNDERLYING_CODE_input.grid(row=10, column=3, padx=5, pady=10)

        self.REMARK_lb = Label(self.input_frame, text="REMARK")
        self.REMARK_lb.grid(row=11, column=0, padx=5, pady=10)
        self.REMARK_input = Entry(self.input_frame)
        self.REMARK_input.grid(row=12, column=0, padx=5, pady=10)

        self.DELETE_FLAG_lb = Label(self.input_frame, text="DELETE_FLAG")
        self.DELETE_FLAG_lb.grid(row=11, column=1, padx=5, pady=10)
        self.DELETE_FLAG_input = ttk.Combobox(self.input_frame,values=["DELETE"],state="readonly")
        self.DELETE_FLAG_input.grid(row=12, column=1, padx=5, pady=10)

        self.append_profiles_btn = Button(self.input_frame, text="Add Data")
        self.append_profiles_btn.grid(row=13, column=0, columnspan=1, padx=10, pady=10)
        
        self.edit_profiles_btn = Button(self.input_frame, text="Edit Data")
        self.edit_profiles_btn.grid(row=13, column=1, columnspan=1, padx=10, pady=10)

        self.del_profiles_btn = Button(self.input_frame, text="Delete Data")
        self.del_profiles_btn.grid(row=13, column=4, columnspan=1, padx=10, pady=10)

        self.home_page_btn = Button(self.input_frame, text="Back to Home")
        self.home_page_btn.grid(row=14, column=0, padx=0, pady=10, sticky="w")



        self.preview_frame = Frame(self,width=400)
        self.preview_frame.grid(row=0, column=1,padx=10,pady=10,sticky="nsew")

        cols = ('REF_NO', 'RULE_CODE', 'RULE_DESCRIPTION', 'FORMULA', 'OPEN_PARENTHESIS',
                    'CONDITION', 'OPERATOR1', 'CONDITION_VALUE', 'AND_OR1', 'CLOSE_PARENTHESIS',
                    'AND_OR2', 'OPERATOR2', 'LIMIT_VALUE', 'BENCHMARK_CODE', 'PRORATA', 'CIS_MANAGER',
                    'MKT_DERIVATIVE', 'UNDERLYING_CODE', 'REMARK', 'DELETE_FLAG', 'USER_UPLOAD', 'UPLOAD_DATE')
        
        self.preview_box = ttk.Treeview(self.preview_frame,
                                        show='headings',
                                        columns=cols,
                                        height=10,
                                        )
        
        for heading in cols:
            self.preview_box.heading(heading, text=heading)
            self.preview_box.column(heading,width=150)

        preview_scroll = ttk.Scrollbar(self.preview_frame, orient="horizontal",command=self.preview_box.xview)
        preview_scroll.pack(side="top",fill='x')
        
        self.preview_box.configure(xscrollcommand=preview_scroll.set)

        self.preview_box.pack(fill="both", expand=True)

        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)
        self.preview_frame.grid_rowconfigure(0, weight=0)
        self.preview_frame.grid_columnconfigure(0, weight=0)



   
    def populate_treeview(self, data):
        # Clear the TreeView
        for item in self.preview_box.get_children():
            self.preview_box.delete(item)
        # Add rows to the TreeView
        for _, row in data.iterrows():
            self.preview_box.insert("", "end", values=row.to_list())

    # Dictionary for dynamic options
        self.options_mapping = {
            "UNIT_TRUST_POLICY" : ["Equity Fund","ESG-SRI ","ETF", "Feeder Fund","Fixed Income Fund","Fund of Funds","Gold Fund","Index Fund","Money Market Fund","Oil Fund"],
            "SUB_SEC_TYPE": ["Basel III","CIS","COLLATERAL","EQ","GOV-BOND","INFRA","Private equity","PROPERTY""REIT","SUKUK","กึ่งหนี้กึ่งทุน"],
            "SEC_RATING_TYPE": ["Short Term","Long Term"],
            "COMPANY_RATING_TYPE": ["Short Term","Long Term"],
            "SEC_NATIONAL_INTER": ["National","Internation"],
            "COMPANY_NATIONAL_INTER": ["National","Internation"],
            "DIVERSIFIED": ["Undiversified","Diversified"],
            "BB_TICKER_CODE": ["Y","N"],
            "SUSPENSE": ["Y","N"]
        }

        self.formula_options_mapping = {
    "(%)GROUP_OF_ASSETS_MKV/NAV": [
        "UNIT_TRUST_POLICY", "PRIMARY_EXCHG", "ISSUER_GROUP_CODE", "SECTOR_CODE",
        "SEC_CLASS", "SUB_SEC_TYPE", "TTM", "COUNTRY_GROUP_CODE", "SEC_RATING_TYPE",
        "COMPANY_RATING_TYPE", "SEC_NATIONAL_INTER", "COMPANY_NATIONAL_INTER",
        "BB_TICKER_CODE", "SEC_RATING_SCORE", "COM_RATING_SCORE_ISSUER",
        "COM_RATING_SCORE_GUARANTEE", "COM_RATING_SCORE_AVAL", "CURRENCY_CODE",
        "SECURITIES_CODE", "SECURITIES_GROUP", "SUSPENSE"
    ],
    "(%)ADVERTISING_EXPENSE/AVG_NAV": [],
    "(%)OTHER_EXPENSE/AVG_NAV": [],
    "(%)CONTRACT_AMT/EXPOSURE(BY_CCY)": [
        "UNIT_TRUST_POLICY", "PRIMARY_EXCHG", "ISSUER_GROUP_CODE", "SECTOR_CODE",
        "SEC_CLASS", "SUB_SEC_TYPE", "TTM", "COUNTRY_GROUP_CODE", "SEC_RATING_TYPE",
        "COMPANY_RATING_TYPE", "SEC_NATIONAL_INTER", "COMPANY_NATIONAL_INTER",
        "BB_TICKER_CODE", "SEC_RATING_SCORE", "COM_RATING_SCORE_ISSUER",
        "COM_RATING_SCORE_GUARANTEE", "COM_RATING_SCORE_AVAL", "CURRENCY_CODE",
        "DIVERSIFIED", "SECURITIES_CODE", "SECURITIES_GROUP"
    ],
    "(%)GLOBAL_EXPOS_LIMIT/NAV(NON_HEDGED)": [],
    "(%)CHANGE_OF_FUND'S_OUTS_UNIT": [],
    "(%)HOLDING_UNIT/OUTS_UNIT(CIS)": [
        "UNIT_TRUST_POLICY", "PRIMARY_EXCHG", "ISSUER_GROUP_CODE", "SECTOR_CODE",
        "SEC_CLASS", "SUB_SEC_TYPE", "TTM", "COUNTRY_GROUP_CODE", "SEC_RATING_TYPE",
        "COMPANY_RATING_TYPE", "SEC_NATIONAL_INTER", "COMPANY_NATIONAL_INTER",
        "BB_TICKER_CODE", "SEC_RATING_SCORE", "COM_RATING_SCORE_ISSUER",
        "COM_RATING_SCORE_GUARANTEE", "COM_RATING_SCORE_AVAL", "CURRENCY_CODE",
        "DIVERSIFIED", "SECURITIES_CODE", "SECURITIES_GROUP"
    ],

    # Group specific to MKV calculations
    "(%)MKV_OF_ASSETS_BY_ISSUER/NAV": [
        "UNIT_TRUST_POLICY", "PRIMARY_EXCHG", "ISSUER_GROUP_CODE", "SECTOR_CODE",
        "SEC_CLASS", "SUB_SEC_TYPE", "TTM", "COUNTRY_GROUP_CODE", "SEC_RATING_TYPE",
        "COMPANY_RATING_TYPE", "SEC_NATIONAL_INTER", "COMPANY_NATIONAL_INTER",
        "BB_TICKER_CODE", "SEC_RATING_SCORE", "COM_RATING_SCORE_ISSUER",
        "COM_RATING_SCORE_GUARANTEE", "COM_RATING_SCORE_AVAL", "CURRENCY_CODE",
        "DIVERSIFIED", "SECURITIES_CODE", "SECURITIES_GROUP", "SUSPENSE"
    ],
    "(%)MKV_OF_ASSETS_BY_ISSUER_GROUP/NAV": [
        "UNIT_TRUST_POLICY", "PRIMARY_EXCHG", "ISSUER_GROUP_CODE", "SECTOR_CODE",
        "SEC_CLASS", "SUB_SEC_TYPE", "TTM", "COUNTRY_GROUP_CODE", "SEC_RATING_TYPE",
        "COMPANY_RATING_TYPE", "SEC_NATIONAL_INTER", "COMPANY_NATIONAL_INTER",
        "BB_TICKER_CODE", "SEC_RATING_SCORE", "COM_RATING_SCORE_ISSUER",
        "COM_RATING_SCORE_GUARANTEE", "COM_RATING_SCORE_AVAL", "CURRENCY_CODE",
        "DIVERSIFIED", "SECURITIES_CODE", "SECURITIES_GROUP", "SUSPENSE"
    ],

    # Additional mappings
    "(%)MKV_OF_SAME_AMC_CIS_INVEST/NAV": [
        "UNIT_TRUST_POLICY", "PRIMARY_EXCHG", "ISSUER_GROUP_CODE", "SECTOR_CODE",
        "SEC_CLASS", "SUB_SEC_TYPE", "TTM", "COUNTRY_GROUP_CODE", "SEC_RATING_TYPE",
        "COMPANY_RATING_TYPE", "SEC_NATIONAL_INTER", "COMPANY_NATIONAL_INTER",
        "BB_TICKER_CODE", "SEC_RATING_SCORE", "COM_RATING_SCORE_ISSUER",
        "COM_RATING_SCORE_GUARANTEE", "COM_RATING_SCORE_AVAL", "CURRENCY_CODE",
        "DIVERSIFIED", "SECURITIES_CODE", "SECURITIES_GROUP"
    ],
    "(#OF_FLOW)_OF_SAME_AMC_CIS_INV": [
        "UNIT_TRUST_POLICY", "PRIMARY_EXCHG", "ISSUER_GROUP_CODE", "SECTOR_CODE",
        "SEC_CLASS", "SUB_SEC_TYPE", "TTM", "COUNTRY_GROUP_CODE", "SEC_RATING_TYPE",
        "COMPANY_RATING_TYPE", "SEC_NATIONAL_INTER", "COMPANY_NATIONAL_INTER",
        "BB_TICKER_CODE", "SEC_RATING_SCORE", "COM_RATING_SCORE_ISSUER",
        "COM_RATING_SCORE_GUARANTEE", "COM_RATING_SCORE_AVAL", "CURRENCY_CODE",
        "DIVERSIFIED", "SECURITIES_CODE", "SECURITIES_GROUP"
    ],

    # Other unique mappings
    "(%)LIMIT_FROM_BENCHMARK_CAL": [],
    "(%)HOLDING_NOMINAL_AMT_BY_ISSUER/TOTAL_FIN_LIAB": [
        "UNIT_TRUST_POLICY", "PRIMARY_EXCHG", "ISSUER_GROUP_CODE", "SECTOR_CODE",
        "SEC_CLASS", "SUB_SEC_TYPE", "TTM", "COUNTRY_GROUP_CODE", "SEC_RATING_TYPE",
        "COMPANY_RATING_TYPE", "SEC_NATIONAL_INTER", "COMPANY_NATIONAL_INTER",
        "BB_TICKER_CODE", "SEC_RATING_SCORE", "COM_RATING_SCORE_ISSUER",
        "COM_RATING_SCORE_GUARANTEE", "COM_RATING_SCORE_AVAL", "CURRENCY_CODE",
        "DIVERSIFIED", "SECURITIES_CODE", "SECURITIES_GROUP"
    ],
    "(DAYS)PORTFOLIO_MACAULAY_DURATION": [
        "UNIT_TRUST_POLICY", "PRIMARY_EXCHG", "ISSUER_GROUP_CODE", "SECTOR_CODE",
        "SEC_CLASS", "SUB_SEC_TYPE", "TTM", "COUNTRY_GROUP_CODE", "SEC_RATING_TYPE",
        "COMPANY_RATING_TYPE", "SEC_NATIONAL_INTER", "COMPANY_NATIONAL_INTER",
        "BB_TICKER_CODE", "SEC_RATING_SCORE", "COM_RATING_SCORE_ISSUER",
        "COM_RATING_SCORE_GUARANTEE", "COM_RATING_SCORE_AVAL", "CURRENCY_CODE",
        "DIVERSIFIED", "SECURITIES_CODE", "SECURITIES_GROUP"
    ]
}

    

    def update_second_combobox(self, event):
        """Update the second combobox based on the first combobox selection."""
        selected_value = self.CONDITION_input.get()
        if selected_value in self.options_mapping:
            # Update second combobox options dynamically
            self.CONDITION_VALUE_input['values'] = self.options_mapping[selected_value]
            self.CONDITION_VALUE_input.set("")  # Clear the current selection
        else:
            # If no mapping exists, allow manual input
            self.CONDITION_VALUE_input['values'] = []  # Clear dropdown values
            self.CONDITION_VALUE_input.set("")  # Clear current selection
    

            '''
                    self.fumula_options_mapping = {
                        "(%)GROUP_OF_ASSETS_MKV/NAV" : ["UNIT_TRUST_POLICY",
                                                        "PRIMARY_EXCHG",
                                                        "ISSUER_GROUP_CODE",
                                                        "SECTOR_CODE",
                                                        "SEC_CLASS",
                                                        "SUB_SEC_TYPE ",
                                                        "TTM",
                                                        "COUNTRY_GROUP_CODE",
                                                        "SEC_RATING_TYPE",
                                                        "COMPANY_RATING_TYPE ",
                                                        "SEC_NATIONAL_INTER ",
                                                        "COMPANY_NATIONAL_INTER",
                                                        "BB_TICKER_CODE",
                                                        "SEC_RATING_SCORE",
                                                        "COM_RATING_SCORE_ISSUER ",
                                                        "COM_RATING_SCORE_GUARANTEE",
                                                        "COM_RATING_SCORE_AVAL  ",
                                                        "CURRENCY_CODE",
                                                        "SECURITIES_CODE",
                                                        "SECURITIES_GROUP",
                                                        "SUSPENSE"],
                        "(%)ADVERTISING_EXPENSE/AVG_NAV":[""
                                                        ],
                        "(%)OTHER_EXPENSE/AVG_NAV":[""
                                                    ],
                        "(%)CONTRACT_AMT/EXPOSURE(BY_CCY)":["UNIT_TRUST_POLICY",
                                                            "PRIMARY_EXCHG",
                                                            "ISSUER_GROUP_CODE",
                                                            "SECTOR_CODE",
                                                            "SEC_CLASS",
                                                            "SUB_SEC_TYPE ",
                                                            "TTM",
                                                            "COUNTRY_GROUP_CODE",
                                                            "SEC_RATING_TYPE",
                                                            "COMPANY_RATING_TYPE ",
                                                            "SEC_NATIONAL_INTER ",
                                                            "COMPANY_NATIONAL_INTER",
                                                            "BB_TICKER_CODE",
                                                            "SEC_RATING_SCORE",
                                                            "COM_RATING_SCORE_ISSUER ",
                                                            "COM_RATING_SCORE_GUARANTEE",
                                                            "COM_RATING_SCORE_AVAL  ",
                                                            "CURRENCY_CODE",
                                                            "DIVERSIFIED",
                                                            "SECURITIES_CODE",
                                                            "SECURITIES_GROUP"
                                                            ],
                        "(%)GLOBAL_EXPOS_LIMIT/NAV(NON_HEDGED)":[""
                                                                            
                                                                ],    
                        "(%)CHANGE_OF_FUND'S_OUTS_UNIT":[""
                                                        ],
                
                        "(%)HOLDING_UNIT/OUTS_UNIT(CIS)":["UNIT_TRUST_POLICY",
                                                            "PRIMARY_EXCHG",
                                                            "ISSUER_GROUP_CODE",
                                                            "SECTOR_CODE",
                                                            "SEC_CLASS",
                                                            "SUB_SEC_TYPE ",
                                                            "TTM",
                                                            "COUNTRY_GROUP_CODE",
                                                            "SEC_RATING_TYPE",
                                                            "COMPANY_RATING_TYPE ",
                                                            "SEC_NATIONAL_INTER ",
                                                            "COMPANY_NATIONAL_INTER",
                                                            "BB_TICKER_CODE",
                                                            "SEC_RATING_SCORE",
                                                            "COM_RATING_SCORE_ISSUER ",
                                                            "COM_RATING_SCORE_GUARANTEE",
                                                            "COM_RATING_SCORE_AVAL  ",
                                                            "CURRENCY_CODE",
                                                            "DIVERSIFIED",
                                                            "SECURITIES_CODE",
                                                            "SECURITIES_GROUP",

                                                        ],      
                    "(%)MKV_OF_ASSETS_BY_ISSUER/NAV":["UNIT_TRUST_POLICY",
                                                        "PRIMARY_EXCHG",
                                                        "ISSUER_GROUP_CODE",
                                                        "SECTOR_CODE",
                                                        "SEC_CLASS",
                                                        "SUB_SEC_TYPE ",
                                                        "TTM",
                                                        "COUNTRY_GROUP_CODE",
                                                        "SEC_RATING_TYPE",
                                                        "COMPANY_RATING_TYPE ",
                                                        "SEC_NATIONAL_INTER ",
                                                        "COMPANY_NATIONAL_INTER",
                                                        "BB_TICKER_CODE",
                                                        "SEC_RATING_SCORE",
                                                        "COM_RATING_SCORE_ISSUER ",
                                                        "COM_RATING_SCORE_GUARANTEE",
                                                        "COM_RATING_SCORE_AVAL  ",
                                                        "CURRENCY_CODE",
                                                        "DIVERSIFIED",
                                                        "SECURITIES_CODE",
                                                        "SECURITIES_GROUP",
                                                        "SUSPENSE"
                                                        ],
                    "(%)MKV_OF_ASSETS_BY_ISSUER_GROUP/NAV":["UNIT_TRUST_POLICY",
                                                        "PRIMARY_EXCHG",
                                                        "ISSUER_GROUP_CODE",
                                                        "SECTOR_CODE",
                                                        "SEC_CLASS",
                                                        "SUB_SEC_TYPE ",
                                                        "TTM",
                                                        "COUNTRY_GROUP_CODE",
                                                        "SEC_RATING_TYPE",
                                                        "COMPANY_RATING_TYPE ",
                                                        "SEC_NATIONAL_INTER ",
                                                        "COMPANY_NATIONAL_INTER",
                                                        "BB_TICKER_CODE",
                                                        "SEC_RATING_SCORE",
                                                        "COM_RATING_SCORE_ISSUER ",
                                                        "COM_RATING_SCORE_GUARANTEE",
                                                        "COM_RATING_SCORE_AVAL  ",
                                                        "CURRENCY_CODE",
                                                        "DIVERSIFIED",
                                                        "SECURITIES_CODE",
                                                        "SECURITIES_GROUP",
                                                        "SUSPENSE"
                                                        ],
                        "(%)MKV_OF_SAME_AMC_CIS_INVEST/NAV":["UNIT_TRUST_POLICY",
                                                        "PRIMARY_EXCHG",
                                                        "ISSUER_GROUP_CODE",
                                                        "SECTOR_CODE",
                                                        "SEC_CLASS",
                                                        "SUB_SEC_TYPE ",
                                                        "TTM",
                                                        "COUNTRY_GROUP_CODE",
                                                        "SEC_RATING_TYPE",
                                                        "COMPANY_RATING_TYPE ",
                                                        "SEC_NATIONAL_INTER ",
                                                        "COMPANY_NATIONAL_INTER",
                                                        "BB_TICKER_CODE",
                                                        "SEC_RATING_SCORE",
                                                        "COM_RATING_SCORE_ISSUER ",
                                                        "COM_RATING_SCORE_GUARANTEE",
                                                        "COM_RATING_SCORE_AVAL  ",
                                                        "CURRENCY_CODE",
                                                        "DIVERSIFIED",
                                                        "SECURITIES_CODE",
                                                        "SECURITIES_GROUP",
                                                        ],
                    "(#OF_FLOW)_OF_SAME_AMC_CIS_INV":["UNIT_TRUST_POLICY",
                                                        "PRIMARY_EXCHG",
                                                        "ISSUER_GROUP_CODE",
                                                        "SECTOR_CODE",
                                                        "SEC_CLASS",
                                                        "SUB_SEC_TYPE ",
                                                        "TTM",
                                                        "COUNTRY_GROUP_CODE",
                                                        "SEC_RATING_TYPE",
                                                        "COMPANY_RATING_TYPE ",
                                                        "SEC_NATIONAL_INTER ",
                                                        "COMPANY_NATIONAL_INTER",
                                                        "BB_TICKER_CODE",
                                                        "SEC_RATING_SCORE",
                                                        "COM_RATING_SCORE_ISSUER ",
                                                        "COM_RATING_SCORE_GUARANTEE",
                                                        "COM_RATING_SCORE_AVAL  ",
                                                        "CURRENCY_CODE",
                                                        "DIVERSIFIED",
                                                        "SECURITIES_CODE",
                                                        "SECURITIES_GROUP",
                                                        ],
                "(%)FUND_TYPE_LIMIT(AVERAGE_รอบปี)":["UNIT_TRUST_POLICY",
                                                        "PRIMARY_EXCHG",
                                                        "ISSUER_GROUP_CODE",
                                                        "SECTOR_CODE",
                                                        "SEC_CLASS",
                                                        "SUB_SEC_TYPE ",
                                                        "TTM",
                                                        "COUNTRY_GROUP_CODE",
                                                        "SEC_RATING_TYPE",
                                                        "COMPANY_RATING_TYPE ",
                                                        "SEC_NATIONAL_INTER ",
                                                        "COMPANY_NATIONAL_INTER",
                                                        "BB_TICKER_CODE",
                                                        "SEC_RATING_SCORE",
                                                        "COM_RATING_SCORE_ISSUER ",
                                                        "COM_RATING_SCORE_GUARANTEE",
                                                        "COM_RATING_SCORE_AVAL  ",
                                                        "CURRENCY_CODE",
                                                        "DIVERSIFIED",
                                                        "SECURITIES_CODE",
                                                        "SECURITIES_GROUP",
                                                        ],
                    "(%)HOLDING_NOMINAL_AMT_BY_ISSUER/TOTAL_FIN_LIAB":["UNIT_TRUST_POLICY",
                                                        "PRIMARY_EXCHG",
                                                        "ISSUER_GROUP_CODE",
                                                        "SECTOR_CODE",
                                                        "SEC_CLASS",
                                                        "SUB_SEC_TYPE ",
                                                        "TTM",
                                                        "COUNTRY_GROUP_CODE",
                                                        "SEC_RATING_TYPE",
                                                        "COMPANY_RATING_TYPE ",
                                                        "SEC_NATIONAL_INTER ",
                                                        "COMPANY_NATIONAL_INTER",
                                                        "BB_TICKER_CODE",
                                                        "SEC_RATING_SCORE",
                                                        "COM_RATING_SCORE_ISSUER ",
                                                        "COM_RATING_SCORE_GUARANTEE",
                                                        "COM_RATING_SCORE_AVAL  ",
                                                        "CURRENCY_CODE",
                                                        "DIVERSIFIED",
                                                        "SECURITIES_CODE",
                                                        "SECURITIES_GROUP",
                                                        ],
                "(%)HOLDING_NOMINAL_AMT/ISSUE_SIZE":["UNIT_TRUST_POLICY",
                                                        "PRIMARY_EXCHG",
                                                        "ISSUER_GROUP_CODE",
                                                        "SECTOR_CODE",
                                                        "SEC_CLASS",
                                                        "SUB_SEC_TYPE ",
                                                        "TTM",
                                                        "COUNTRY_GROUP_CODE",
                                                        "SEC_RATING_TYPE",
                                                        "COMPANY_RATING_TYPE ",
                                                        "SEC_NATIONAL_INTER ",
                                                        "COMPANY_NATIONAL_INTER",
                                                        "BB_TICKER_CODE",
                                                        "SEC_RATING_SCORE",
                                                        "COM_RATING_SCORE_ISSUER ",
                                                        "COM_RATING_SCORE_GUARANTEE",
                                                        "COM_RATING_SCORE_AVAL  ",
                                                        "CURRENCY_CODE",
                                                        "DIVERSIFIED",
                                                        "SECURITIES_CODE",
                                                        "SECURITIES_GROUP",
                                                        ],
                "(DAYS)PORTFOLIO_MACAULAY_DURATION":["UNIT_TRUST_POLICY",
                                                        "PRIMARY_EXCHG",
                                                        "ISSUER_GROUP_CODE",
                                                        "SECTOR_CODE",
                                                        "SEC_CLASS",
                                                        "SUB_SEC_TYPE ",
                                                        "TTM",
                                                        "COUNTRY_GROUP_CODE",
                                                        "SEC_RATING_TYPE",
                                                        "COMPANY_RATING_TYPE ",
                                                        "SEC_NATIONAL_INTER ",
                                                        "COMPANY_NATIONAL_INTER",
                                                        "BB_TICKER_CODE",
                                                        "SEC_RATING_SCORE",
                                                        "COM_RATING_SCORE_ISSUER ",
                                                        "COM_RATING_SCORE_GUARANTEE",
                                                        "COM_RATING_SCORE_AVAL  ",
                                                        "CURRENCY_CODE",
                                                        "DIVERSIFIED",
                                                        "SECURITIES_CODE",
                                                        "SECURITIES_GROUP",
                                                        ],                                             
                "DUP_SELLING_FEE_FOR_SAME_AMC_CIS_INVEST":[""
                                                    ],                                                
                                                            
                "(%)LIMIT_FROM_BENCHMARK_CAL":[""
                                                    ],  
                "(%)FUND_TYPE_LIMIT(AVERAGE_รอบปี)(PRODUCT)":["UNIT_TRUST_POLICY",
                                                        "PRIMARY_EXCHG",
                                                        "ISSUER_GROUP_CODE",
                                                        "SECTOR_CODE",
                                                        "SEC_CLASS",
                                                        "SUB_SEC_TYPE ",
                                                        "TTM",
                                                        "COUNTRY_GROUP_CODE",
                                                        "SEC_RATING_TYPE",
                                                        "COMPANY_RATING_TYPE ",
                                                        "SEC_NATIONAL_INTER ",
                                                        "COMPANY_NATIONAL_INTER",
                                                        "BB_TICKER_CODE",
                                                        "SEC_RATING_SCORE",
                                                        "COM_RATING_SCORE_ISSUER ",
                                                        "COM_RATING_SCORE_GUARANTEE",
                                                        "COM_RATING_SCORE_AVAL  ",
                                                        "CURRENCY_CODE",
                                                        "DIVERSIFIED",
                                                        "SECURITIES_CODE",
                                                        "SECURITIES_GROUP",
                                                        ],      
                "(%)GROUP_OF_ASSETS_MKV/NAV(PRODUCT)":["UNIT_TRUST_POLICY",
                                                        "PRIMARY_EXCHG",
                                                        "ISSUER_GROUP_CODE",
                                                        "SECTOR_CODE",
                                                        "SEC_CLASS",
                                                        "SUB_SEC_TYPE ",
                                                        "TTM",
                                                        "COUNTRY_GROUP_CODE",
                                                        "SEC_RATING_TYPE",
                                                        "COMPANY_RATING_TYPE ",
                                                        "SEC_NATIONAL_INTER ",
                                                        "COMPANY_NATIONAL_INTER",
                                                        "BB_TICKER_CODE",
                                                        "SEC_RATING_SCORE",
                                                        "COM_RATING_SCORE_ISSUER ",
                                                        "COM_RATING_SCORE_GUARANTEE",
                                                        "COM_RATING_SCORE_AVAL  ",
                                                        "CURRENCY_CODE",
                                                        "DIVERSIFIED",
                                                        "SECURITIES_CODE",
                                                        "SECURITIES_GROUP",
                                                        "SUSPENSE"]               
                                                    
                    }
            '''

    
    def update_condition_combobox(self, event):
        """Update the second combobox based on the first combobox selection."""
        selected_value = self.fomula_input.get()
        if selected_value in self.formula_options_mapping:
            # Update second combobox options dynamically
            self.CONDITION_input['values'] = self.formula_options_mapping[selected_value]
            self.CONDITION_input.set("")  # Clear the current selection
        else:
            # If no mapping exists, allow manual input
            self.CONDITION_input['values'] = ["UNIT_TRUST_POLICY",
                                            "PRIMARY_EXCHG",
                                            "ISSUER_GROUP_CODE",
                                            "SECTOR_CODE",
                                            "SEC_CLASS",
                                            "SUB_SEC_TYPE ",
                                            "TTM",
                                            "COUNTRY_GROUP_CODE",
                                            "SEC_RATING_TYPE",
                                            "COMPANY_RATING_TYPE ",
                                            "SEC_NATIONAL_INTER ",
                                            "COMPANY_NATIONAL_INTER",
                                            "BB_TICKER_CODE",
                                            "SEC_RATING_SCORE",
                                            "COM_RATING_SCORE_ISSUER ",
                                            "COM_RATING_SCORE_GUARANTEE",
                                            "COM_RATING_SCORE_AVAL  ",
                                            "CURRENCY_CODE",
                                            "DIVERSIFIED",
                                            "SECURITIES_CODE",
                                            "SECURITIES_GROUP",
                                            "SUSPENSE"]  # Clear dropdown values
            self.CONDITION_input.set("")  # Clear current selection