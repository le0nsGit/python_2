
    ms_dl = open_csv_file()

    output_by_state(ms_dl)

    output_by_race(ms_dl)

    send_to_json_file(ms_dl)