import { useRouter } from 'vue-router';

export const useRouteHandler = () => {
    const R = useRouter();
    const handleRoute = (routeName: string, idC: string, nameC: string) => {
        if (idC) {
            R.push({
                name: routeName + '-id',
                params: {
                    idC: idC,
                    Cname: nameC,
                },
            });
        } else {
            R.push({
                name: routeName,
            });
        }
    };

    return {
        handleRoute,
    };
};
