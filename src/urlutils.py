# __pragma__ ('skip')
class window:
    fetch = None
    encodeURIComponent = None

class console:
    log = None
    error = None

class JSON:
    stringify = None
# __pragma__ ('noskip')


# polyfill = require("@babel/polyfill")  # required by async/await


# __pragma__ ('kwargs')
async def fetch(url, callback=None, **kwargs):
    on_error = kwargs.pop('onError', None)
    method = kwargs.pop('method', 'GET')
    try:
        if method == 'POST' or method == 'DELETE':
            data = kwargs.pop('data', None)
            # headers needs to be a plain JS object
            headers = {'Content-Type': 'application/json;'}  # __:jsiter
            response = await window.fetch(url, {'method': method,
                                                'headers': headers,
                                                'body': JSON.stringify(data)
                                                }
                                          )
        else:
            kw_params = kwargs.pop('params', {})
            params = buildParams(kw_params)
            response = await window.fetch(f"{url}{params}")

        if response.status == 401:
            console.error("401 - Session Expired")
            raise Exception("Unauthorized")
        elif response.status != 200:
            console.error('Fetch error - Status Code: ' + response.status)
            if on_error:
                on_error()
        else:
            json_data = await response.json()
            error = dict(json_data).get('error', None)
            if error:
                raise Exception(error)
            else:
                if callback:
                    callback(json_data)
    except object as e:
        console.error(str(e))
        if on_error:
            on_error()

# __pragma__ ('nokwargs')


def buildParams(param_dict: dict):
    param_list = [f"&{key}={window.encodeURIComponent(val)}"
                  for key, val in param_dict.items() if val]
    params = ''.join(param_list)
    return f"?{params[1:]}" if len(params) > 0 else ''
