import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.timer_trigger(schedule="0 */1 * * * *", arg_name="myTimer", run_on_startup=True, use_monitor=False) 
def timer_trigger(myTimer: func.TimerRequest) -> None:
    from datetime import datetime
    
    print('='*50)
    print(f'⏰ Timer executado em: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    print('='*50)
    
    logging.info('Python timer trigger function executed.')
    
    if myTimer.past_due:
        print('⚠️ O timer está atrasado!')
        logging.warning('The timer is past due!')
    
    # Log informações sobre o próximo agendamento
    if myTimer.schedule_status:
        print(f'📅 Próxima execução: {myTimer.schedule_status.next}')
        print(f'📅 Última execução: {myTimer.schedule_status.last}')
        logging.info(f'Próxima execução: {myTimer.schedule_status.next}')
        logging.info(f'Última execução: {myTimer.schedule_status.last}')